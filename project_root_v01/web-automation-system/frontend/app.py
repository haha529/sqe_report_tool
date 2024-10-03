import streamlit as st
import requests
from logging_config import setup_logging
import logging

setup_logging()

st.title("Web Automation System")
logging.info("Web Automation System started")

# Load email templates
response = requests.get("http://localhost:8000/templates")
templates = response.json().get("templates", [])

# Display template list
template_choice = st.selectbox("Choose an Email Template", templates)

if template_choice:
    response = requests.get(f"http://localhost:8000/template/{template_choice}")
    template_content = response.json().get("content", "")
    new_content = st.text_area("Email Template Content", template_content, height=300)

    if st.button("Save Template"):
        response = requests.post(f"http://localhost:8000/template/{template_choice}", json={"content": new_content})
        st.success("Template saved successfully")

    custom_text = st.text_area("Custom Text")
    images = st.text_area("Images (comma separated)").split(',')
    recipient = st.text_input("Recipient Email")

    if st.button("Send Email"):
        response = requests.post("http://localhost:8000/send-email", json={
            "template": template_choice,
            "recipient": recipient,
            "images": images,
            "custom_text": custom_text
        })
        st.write(response.json())