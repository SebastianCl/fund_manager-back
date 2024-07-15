import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client # type: ignore
import os


class NotificationSender:
    EMAIL_CONFIG = {
        "from_email": os.getenv("EMAIL_USER"),
        "email_password": os.getenv("EMAIL_PASS"),
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
    }

    SMS_CONFIG = {
        "account_sid": os.getenv("TWILIO_SID"),
        "auth_token": os.getenv("TWILIO_AUTH"),
        "from_phone": os.getenv("TWILIO_PHONE"),
    }

    @classmethod
    def send_email(cls, to_email, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = cls.EMAIL_CONFIG["from_email"]
        msg["To"] = to_email

        try:
            with smtplib.SMTP(
                cls.EMAIL_CONFIG["smtp_server"], cls.EMAIL_CONFIG["smtp_port"]
            ) as server:
                server.starttls()
                server.login(
                    cls.EMAIL_CONFIG["from_email"], cls.EMAIL_CONFIG["email_password"]
                )
                server.sendmail(
                    cls.EMAIL_CONFIG["from_email"], to_email, msg.as_string()
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")

    @classmethod
    def send_sms(cls, to_phone, body):
        client = Client(cls.SMS_CONFIG["account_sid"], cls.SMS_CONFIG["auth_token"])
        try:
            message = client.messages.create(
                body=body, from_=cls.SMS_CONFIG["from_phone"], to=to_phone
            )
            print("SMS sent successfully!")
        except Exception as e:
            print(f"Failed to send SMS: {e}")
