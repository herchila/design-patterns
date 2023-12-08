class Handler:
    """Abstract Handler: inherited by all concrete handlers."""
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        if not self.can_handle(request):
            if self._successor is not None:
                self._successor.handle_request(request)

    def can_handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class HardwareSupportHandler(Handler):
    """Concrete handler: handles hardware support requests."""
    def can_handle(self, request):
        return request == "Hardware Support"


class SoftwareSupportHandler(Handler):
    """Concrete handler: handles software support requests."""
    def can_handle(self, request):
        return request == "Software Support"


class AccountSupportHandler(Handler):
    """Concrete handler: handles account support requests."""
    def can_handle(self, request):
        return request == "Account Support"


# Create handlers
hardware_handler = HardwareSupportHandler()
software_handler = SoftwareSupportHandler(hardware_handler)
account_handler = AccountSupportHandler(software_handler)

# Client code
def client_code(handler, request):
    print(f"Processing request for {request}")
    handler.handle_request(request)

# Test our chain
client_code(account_handler, "Hardware Support")
client_code(account_handler, "Software Support")
client_code(account_handler, "Account Support")
