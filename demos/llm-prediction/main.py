import numpy as np
from collections import Counter

from datasets import load_dataset

from transformers import (
    AutoTokenizer,
    DataCollatorWithPadding,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)

from huggingface_hub import notebook_login

notebook_login()


def preprocess_function(rows):
    return tokenizer(rows["text"])


# Load in datasets from Hugging Face
emotion_train = load_dataset("dair-ai/emotion", split="train", trust_remote_code=True)
emotion_val = load_dataset("dair-ai/emotion", split="validation", trust_remote_code=True)
emotion_test = load_dataset("dair-ai/emotion", split="test", trust_remote_code=True)

# Check class balance in training outcome
Counter(emotion_train["label"])

# Read in the AutoTokeniser
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

# Tokenise the train and validation data using the AutoTokeniser
tokenized_train = emotion_train.map(preprocess_function, batched=True)
tokenized_val = emotion_val.map(preprocess_function, batched=True)
tokenized_test = emotion_test.map(preprocess_function, batched=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Set up model training
batch_size = 16
metric_name = "f1"

training_args = TrainingArguments(
    "bert-fine-tuned-emotion-classification-english",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=10,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model=metric_name,
    push_to_hub=True,
)

from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
from transformers import EvalPrediction
import torch


# source: https://jesusleal.io/2021/04/21/Longformer-multilabel-classification/
def multi_label_metrics(predictions, labels, threshold=0.5):
    # first, apply sigmoid on predictions which are of shape (batch_size, num_labels)
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(torch.Tensor(predictions))
    # next, use threshold to turn them into integer predictions
    y_pred = np.zeros(probs.shape)
    y_pred[np.where(probs >= threshold)] = 1
    # finally, compute metrics
    y_true = labels
    f1_micro_average = f1_score(y_true=y_true, y_pred=y_pred, average='micro')
    roc_auc = roc_auc_score(y_true, y_pred, average='micro')
    accuracy = accuracy_score(y_true, y_pred)
    # return as dictionary
    metrics = {'f1': f1_micro_average,
               'roc_auc': roc_auc,
               'accuracy': accuracy}
    return metrics


def compute_metrics(p: EvalPrediction):
    preds = p.predictions[0] if isinstance(p.predictions,
                                           tuple) else p.predictions
    result = multi_label_metrics(
        predictions=preds,
        labels=p.label_ids)
    return result


id2label = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
label2id = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert/distilbert-base-uncased", num_labels=2, id2label=id2label, label2id=label2id
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=emotion_train,
    eval_dataset=emotion_val,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()
