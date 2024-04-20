import os
from dotenv import load_dotenv
import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

followed_users = 0

def send_email():
    global followed_users  # Declare followed_users as global
    followed_users += 1
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "datchguest@gmail.com"
    receiver_email = "datchdatch2001@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "GitHub Report to DATCH"
    body = f"Total followed users now are {followed_users}"
    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

while True:
    send_email()
    print(f"\nReport sent successfully.\nRef: #{followed_users}\n")
    time.sleep(30)