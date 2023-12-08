class Component:
    def operation(self): pass

class ConcreteComponent(Component):
    def operation(self):
        print("Basic Operation")

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

class AdditionalFeatureDecorator(Decorator):
    def operation(self):
        print("Additional Feature")
        super().operation()

# Usage
simple = ConcreteComponent()
decorated = AdditionalFeatureDecorator(simple)
decorated.operation()  # Additional Feature\nBasic Operation
