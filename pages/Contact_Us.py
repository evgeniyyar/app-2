import streamlit
from send_email import send_email


streamlit.header("Contact Me")

with streamlit.form(key="email_forms"):
    user_email = streamlit.text_input("Your email address")
    message = streamlit.text_area("Your message")
    button = streamlit.form_submit_button("Submit")
    if button:
        send_email(message)
        streamlit.info("Your email was sent successfully")
