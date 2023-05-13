# Flask Email Sender

This is a simple Flask application that provides an API endpoint to send an email via an SMTP server.

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Install the required Python libraries using pip:

    ```
    pip install flask
    ```

3. Run the application:

    ```
    python app.py
    ```

    The application will start on `localhost` port `5000`.

## API Endpoints

### POST /send_email

Sends an email using the provided SMTP server credentials and email details.

#### Parameters

The parameters should be sent as JSON in the body of the POST request.

- `smtp_server`: The SMTP server to connect to.
- `port`: The port to use for the SMTP server.
- `sender_email`: The email address of the sender.
- `sender_password`: The password for the sender's email account.
- `receiver_email`: The email address of the receiver.
- `subject`: The subject of the email.
- `message`: The body of the email, in HTML format.

#### Example

Here is an example of the JSON data to send in the POST request:

```json
{
    "smtp_server": "smtp.server.com",
    "port": 465,
    "sender_email": "sender@example.com",
    "sender_password": "password",
    "receiver_email": "receiver@example.com",
    "subject": "Email Subject",
    "message": "<h1>Hello, World!</h1>"
}

The `README.md` file should provide all the necessary information for someone else to understand how to run and use your application.
