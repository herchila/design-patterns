import copy

class Prototype:
    def clone(self): pass

class ConcretePrototype(Prototype):
    def __init__(self, number):
        self.number = number

    def clone(self):
        return copy.deepcopy(self)

# Usage
prototype = ConcretePrototype(1)
cloned_prototype = prototype.clone()
print(cloned_prototype.number)  # Output: 1
