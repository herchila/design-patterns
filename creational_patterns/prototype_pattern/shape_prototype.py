import copy

class ShapePrototype:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Shape: X={self.x}, Y={self.y}, Color={self.color}"

# Prototype registry
class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, shape_id, shape):
        self._prototypes[shape_id] = shape

    def unregister(self, shape_id):
        del self._prototypes[shape_id]

    def clone(self, shape_id, **attributes):
        shape = copy.deepcopy(self._prototypes.get(shape_id))
        shape.__dict__.update(attributes)
        return shape

# Client code
registry = PrototypeRegistry()
circle_prototype = ShapePrototype(0, 0, "Red")
registry.register("Circle", circle_prototype)

# Cloning a circle and modifying its properties
cloned_circle = registry.clone("Circle", x=10, y=20, color="Blue")
print(cloned_circle)  # Shape: X=10, Y=20, Color=Blue
