import streamlit as sl

sl.header("contact me!")

with sl.form(key="email_form"):
    email = sl.text_input("your email address")
    message = sl.text_area("your message")
    button = sl.form_submit_button("submit")
    if button:
        send = message + email
