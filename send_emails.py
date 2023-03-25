import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "aleksic.strahinja06@gmail.com"
    passwords = os.getenv("PORTFOLIOPASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, passwords)
        server.sendmail(username, "strale.alek@gmail.com", message)