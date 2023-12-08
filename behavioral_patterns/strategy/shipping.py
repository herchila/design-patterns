from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    """Abstract base class for shipping strategies."""
    
    @abstractmethod
    def calculate(self, order):
        pass


class StandardShipping(ShippingStrategy):
    """Concrete strategy for standard shipping."""
    
    def calculate(self, order):
        return 5.00  # Flat rate


class ExpeditedShipping(ShippingStrategy):
    """Concrete strategy for expedited shipping."""
    
    def calculate(self, order):
        return 10.00  # Flat rate

class InternationalShipping(ShippingStrategy):
    """Concrete strategy for international shipping."""
    
    def calculate(self, order):
        return 20.00  # Flat rate


class Order:
    """Client class that uses a shipping strategy."""
    
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate_shipping_cost(self):
        return self.strategy.calculate(self)


# Usage
# Client code
standard_order = Order(StandardShipping())
print(f"Standard Shipping Cost: {standard_order.calculate_shipping_cost()}")

expedited_order = Order(ExpeditedShipping())
print(f"Expedited Shipping Cost: {expedited_order.calculate_shipping_cost()}")

international_order = Order(InternationalShipping())
print(f"International Shipping Cost: {international_order.calculate_shipping_cost()}")
