import os
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client  # type: ignore


class NotificationSender:
    def __init__(self):
        self.email_config = {
            "from_email": os.getenv("GMAIL_FROM_EMAIL"),
            "email_password": os.getenv("GMAIL_EMAIL_PASSWORD"),
            "smtp_server": os.getenv("GMAIL_SMTP_SERVER"),
            "smtp_port": os.getenv("GMAIL_SMTP_PORT"),
        }

        self.sms_config = {
            "account_sid": os.getenv("TWILIO_ACCOUNT_SID"),
            "auth_token": os.getenv("TWILIO_AUTH_TOKEN"),
            "from_phone": os.getenv("TWILIO_PHONE"),
        }

    def send_email(self, to_email, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.email_config["from_email"]
        msg["To"] = to_email

        try:
            with smtplib.SMTP(
                self.email_config["smtp_server"], self.email_config["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    self.email_config["from_email"], self.email_config["email_password"]
                )
                server.sendmail(
                    self.email_config["from_email"], to_email, msg.as_string()
                )
            print("Email sent successfully!")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

    def send_sms(self, to_phone, body):
        client = Client(self.sms_config["account_sid"], self.sms_config["auth_token"])
        try:
            message = client.messages.create(
                body=body, from_=self.sms_config["from_phone"], to=to_phone
            )
            print("SMS sent successfully!")
        except Exception as e:
            print(f"Failed to send SMS: {e}")
