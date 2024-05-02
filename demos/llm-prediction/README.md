# PyCon US Hugging Face model card demo

This demo is very straightforward: it is simply designed to show how Hugging Face model cards and dataset cards are available in PyCharm.

## What are dataset and model cards?
Dataset and model cards are detailed descriptions of datasets and models hosted on the Hugging Face hub. This includes important information about the who created the dataset/model, how it was put together, and what usage rights are associated with it. These cards are extremely important when using Hugging Face assets, as they allow you to understand at a glance what the best use cases for these datasets and models are.

Within `emotion-classification.ipynb`, go to:
* Dataset card
  * Cell 3
  * Hover over any mention of `dair-ai/emotion`
  * Dataset card will pop up.
  * You can navigate to the dataset card on Hugging Face Hub by clicking on "Open on Hugging Face".
* Model card
  * Cell 5
  * Hover over distilbert/distilbert-base-uncased`
  * Model card will pop up.
  * You can navigate to the model card on Hugging Face Hub by clicking on "Open on Hugging Face".

You can repeat this exercise in `main.py` to demonstrate that the dataset and model cards also work within Python scripts as well as notebooks.
