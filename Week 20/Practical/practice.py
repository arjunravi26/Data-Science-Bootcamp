from abc import ABC, abstractmethod

# Abstract class for Payment Processors
class PaymentProcessor(ABC):
    @abstractmethod
    def authenticate(self):
        """Authenticate the payment method"""
        pass

    @abstractmethod
    def process_payment(self, amount):
        """Process the payment"""
        pass

# Concrete implementations
class CreditCardPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating Credit Card using bank API...")

    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount} via secure gateway.")

class PayPalPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating PayPal account using OAuth...")

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount} via PayPal API.")

# Function to make payments
def make_payment(payment_processor: PaymentProcessor, amount: float):
    payment_processor.authenticate()
    payment_processor.process_payment(amount)

# Client Code
payment1 = CreditCardPayment()
payment2 = PayPalPayment()

make_payment(payment1, 150.0)  # User doesn't care how CreditCard works
make_payment(payment2, 250.0)  # User doesn't care how PayPal works
