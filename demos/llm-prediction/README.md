# PyCon US Hugging Face model card demo

This demo is very straightforward: it is designed to show three Hugging Face integrations we have built into PyCharm. These are:
* Model selection tool window
* Model cards on hover
* Hugging Face tool window

## What are model cards?
Model cards are detailed descriptions of the models hosted on the Hugging Face hub. This includes important information about who created the model, how it was put together, and what usage rights are associated with it. These cards are extremely important when using Hugging Face assets, as they allow you to understand at a glance what the best use cases for these models are.

## Demo instructions

### Demoing the model selection tool window
* Open `text-classification.ipynb`
* Explain that we're doing a project to classify whether books are fiction or nonfiction, and we're going to use an LLM to do so
* Go to the cell under "Select an LLM from HuggingFace Hub to classify the books". **Make sure you've run everything above this cell, and the cell below as well which reads in the BART model.**
* Explain that we've picked this preliminary BART model, but perhaps we want to see what other options we have for text classification models on Hugging Face.
* In the cell below, right click and select "Insert HF model". Explain that we can see everything here, exactly as we would when doing model selection on Hugging Face Hub.
* Click on "Text Classification" on the left, and show the different models available.
* Show the model cards on the right.
* Select a model other than BART and insert in the cell by clicking "Use Model".

### Demoing the model cards
* Hover over the name of the BART model (facebook/bart-large-mnli). You'll see the model card pop up as quick documentation.
* Explain how this makes it really easy to see the information about the models you're currently using.

### Demoing the Hugging Face tool window
* Click on the Hugging Face icon on the left hand side of the IDE.
* This will show all the models you currently have downloaded.
* Explain how you can use this to manage your models, including downloading ones that are too large.