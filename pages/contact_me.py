import streamlit as sl
from set_email import send_email

sl.header("contact me!")

options = ["experience", "volunteering", "college", "other"]

with sl.form(key="email_form"):
    email = sl.text_input("your email address")
    topic = sl.selectbox("what topic do you want to discuss?", options)
    message = sl.text_area("your message")
    send_message = f"""\
Subject: new email from portfolio

from: {email}
topic: {topic}
{message}
"""
    button = sl.form_submit_button("submit")
    if button:
        send_email(send_message)
        sl.info("your email was sent successfully")
