class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self.check_request(request)
        if not res and self._successor:
            self._successor.handle(request)

    def check_request(self, request): pass

class ConsoleHandler(Handler):
    def check_request(self, request):
        if request < 3:
            print(f"Console: {request}")
            return True

class FileHandler(Handler):
    def check_request(self, request):
        if 3 <= request < 5:
            print(f"File: {request}")
            return True

class EmailHandler(Handler):
    def check_request(self, request):
        if request >= 5:
            print(f"Email: {request}")
            return True

# Usage
chain = ConsoleHandler(FileHandler(EmailHandler()))
chain.handle(2)  # Console: 2
chain.handle(4)  # File: 4
chain.handle(5)  # Email: 5
