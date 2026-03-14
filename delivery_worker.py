class MailboxService:

    def __init__(self):
        self.mailboxes = {}

    def receive_email(self, receiver, email):

        if receiver not in self.mailboxes:
            self.mailboxes[receiver] = []

        self.mailboxes[receiver].append(email)

    def get_inbox(self, user):

        return self.mailboxes.get(user, [])
