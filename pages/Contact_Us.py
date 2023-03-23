import streamlit as st
from send_emails import send_email
st.title("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email adress")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}

"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email has been sent successfully")
