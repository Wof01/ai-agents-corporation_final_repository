import streamlit as st
import requests

# API endpoints
IDEA_EXPANDER_URL = "http://localhost:8000/expand-idea"
WRITER_URL = "http://localhost:8000/write-chapter"

# Streamlit app
st.title("AI Book Creator")

# User input
idea = st.text_input("Enter your book idea:")

if st.button("Create Book"):
    if idea:
        # Call Idea Expander API
        outline_response = requests.post(IDEA_EXPANDER_URL, json={"idea": idea})
        outline = outline_response.json().get("outline")

        # Call Writer API
        chapter_response = requests.post(WRITER_URL, json={"outline": outline, "research": "..."})
        chapter = chapter_response.json().get("chapter")

        # Display the result
        st.write("### Book Chapter")
        st.write(chapter)
    else:
        st.error("Please enter an idea.")
