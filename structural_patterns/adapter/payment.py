class LegacyPayment:
    def process_payment(self, amount):
        print(f"Processing legacy payment of {amount}")


class NewPaymentGateway:
    def make_payment(self, amount):
        print(f"Making new payment of {amount}")


class PaymentAdapter:
    def __init__(self, new_payment_gateway):
        self.new_payment_gateway = new_payment_gateway

    def process_payment(self, amount):
        # Translate (adapt) the method call here
        self.new_payment_gateway.make_payment(amount)


# Existing system code
def process_payments(payment_processor, amount):
    payment_processor.process_payment(amount)

# Old payment system
legacy_payment = LegacyPayment()
process_payments(legacy_payment, 100)

# New payment system with adapter
new_payment_gateway = NewPaymentGateway()
adapted_payment = PaymentAdapter(new_payment_gateway)
process_payments(adapted_payment, 150)
