from flask import Flask, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)


def send_email(smtp_server, port, sender_email, sender_password, receiver_email, subject, message):
    """
    Function to send an email using SMTP server.

    Parameters:
    smtp_server (str): The SMTP server to connect to.
    port (int): The port to use for the SMTP server.
    sender_email (str): The email address of the sender.
    sender_password (str): The password for the sender's email account.
    receiver_email (str): The email address of the receiver.
    subject (str): The subject of the email.
    message (str): The body of the email, in HTML format.

    Returns:
    str: A message indicating whether the email was sent successfully, or the error message if an error occurred.
    """
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject
    email.attach(MIMEText(message, "html"))  # changed "plain" to "html"

    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        server.login(sender_email, sender_password)
        text = email.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return "Email was sent successfully."
    except Exception as e:
        return f"An error occurred while sending the email: {str(e)}"


@app.route('/send_email', methods=['POST'])
def send_email_endpoint():
    """
    Flask endpoint for sending an email. Accepts POST requests with JSON data.

    JSON Data format:
    {
        "smtp_server": "smtp.server.com",
        "port": 465,
        "sender_email": "sender@example.com",
        "sender_password": "password",
        "receiver_email": "receiver@example.com",
        "subject": "Email Subject",
        "message": "<html>...</html>"
    }

    Returns:
    JSON: A JSON object containing a response message.
    """
    if request.method == 'POST':
        data = request.get_json()
        response = send_email(
            data['smtp_server'],
            data['port'],
            data['sender_email'],
            data['sender_password'],
            data['receiver_email'],
            data['subject'],
            data['message']
        )
        return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
