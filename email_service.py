class EmailService:

    def __init__(self):
        self.emails = []

    def send_email(self, sender, receiver, subject, body):

        email = {
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "body": body
        }

        self.emails.append(email)

        return email
