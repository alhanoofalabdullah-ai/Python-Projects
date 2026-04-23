
## main.py

```python
import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 465

sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
app_password = "your_app_password"

subject = "Test Email"
body = "Hello, this is a test email sent using Python."

message = f"""Subject: {subject}

{body}
"""


def send_email():
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully.")

    except Exception as error:
        print(f"Failed to send email: {error}")


if __name__ == "__main__":
    send_email()
