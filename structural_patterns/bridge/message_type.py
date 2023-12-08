class MessageType:
    def send(self, message): pass

class TextMessage(MessageType):
    def send(self, message):
        print(f"Text: {message}")

class EmailMessage(MessageType):
    def send(self, message):
        print(f"Email: {message}")

class MessageSender:
    def __init__(self, message_type):
        self.message_type = message_type

    def send(self, message):
        self.message_type.send(message)


# Usage
text = TextMessage()
email = EmailMessage()

sender = MessageSender(text)
sender.send("Hello World")  # Text: Hello World

sender.message_type = email
sender.send("Hello World")  # Email: Hello World
