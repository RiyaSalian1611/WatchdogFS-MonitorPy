# -*- coding: utf-8 -*-
"""Dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cqac35BCg0LB0SxgtVaUchBI4knzhBFE
"""

pip install streamlit

pip install watchdog

pip install langchain

pip install langchain_community

pip install openai

import streamlit as st
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from langchain.llms import OpenAI
import os


# Initialize OpenAI model for sentiment analysis
llm = OpenAI(openai_api_key="...") # copy your api-key

# Define Watchdog event handler for file system monitoring
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.file_events = []

    def on_any_event(self, event):
        if event.is_directory:
            return
        self.file_events.append((event.event_type, event.src_path))

# Function to analyze sentiment of text using OpenAI model
def analyze_sentiment(text):
    sentiment = llm.sentiment_analysis(text)
    return sentiment

# Function to display dashboard
def main():
    st.title("Real-time Data Analysis Dashboard")

    # Initialize file system event handler
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    # Display file system events
    st.header("File System Events")
    if event_handler.file_events:
        for event_type, event_path in event_handler.file_events:
            st.write(f"- {event_type}: {event_path}")
    else:
        st.write("No recent file system events.")

    # Allow users to enter text for sentiment analysis
    st.header("Sentiment Analysis")
    text_input = st.text_area("Enter text for sentiment analysis:")
    if st.button("Analyze Sentiment"):
        sentiment = analyze_sentiment(text_input)
        st.write("Sentiment Analysis Result:")
        st.write(sentiment)

if __name__ == "__main__":
    main()

pip install pyngrok

