import streamlit as st
import requests

# API endpoints
IDEA_EXPANDER_URL = "https://ai-agents-api-7ghb.onrender.com/expand-idea"
WRITER_URL = "https://ai-agents-api-7ghb.onrender.com/write-chapter"

# Streamlit app
st.title("AI Book Creator")

# User input
idea = st.text_input("Enter your book idea:")

if st.button("Create Book"):
    if idea:
        try:
            # Call Idea Expander API
            outline_response = requests.post(IDEA_EXPANDER_URL, json={"idea": idea})
            outline_response.raise_for_status()  # Raise an error for bad status codes
            outline = outline_response.json().get("outline")

            # Call Writer API
            chapter_response = requests.post(WRITER_URL, json={"outline": outline, "research": "..."})
            chapter_response.raise_for_status()
            chapter = chapter_response.json().get("chapter")

            # Display the result
            st.write("### Book Chapter")
            st.write(chapter)
        except requests.exceptions.RequestException as e:
            st.error(f"Error calling API: {e}")
    else:
        st.error("Please enter an idea.")
