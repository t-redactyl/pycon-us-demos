# PyCon US Explain DataFrame demo

The purpose of this demo is to show a very cool feature unique to PyCharm, which is the `Explain DataFrame` capabilities in the AI Assistant.

To set up:
* Make sure you have the AI Assistant plugin installed, and activated.

To work with this:
* Open `titanic-exploration.ipynb`
* Run All (fastfoward symbol at the top of the notebook)
* Go down to the Titanic DataFrame and press the `Explain DataFrame` button in the upper right hand corner
* This will open a new AI Assistant chat.

The first chat will describe the DataFrame, which is a great start. However, you can follow this up with exploratory questions. Some ideas:
* "What variables would predict whether a person survived?"
* "How can I tell which variables correlate highest with passenger survival?"
* "How can I turn sex into a numeric variable?"
* "What is the relationship between passenger class and fare?"

Stress that this is just the very beginning; we're currently working on an implementation for 2024.2 which will allow the chat to access all variables within the Jupyter environment. In this upcoming implementation, you can also insert code as cells, allowing for a very fluid back and forth between the chat and the notebook.