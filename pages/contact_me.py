import streamlit as sl
from set_email import send_email

sl.header("contact me!")

with sl.form(key="email_form"):
    email = sl.text_input("your email address")
    message = sl.text_area("your message")
    send_message = f"""\
Subject: new email from portfolio

from: {email}
{message}
"""
    button = sl.form_submit_button("submit")
    if button:
        send_email(send_message)
        sl.info("your email was sent successfully")
