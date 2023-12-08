class Graphic:
    def render(self): pass

class Circle(Graphic):
    def render(self):
        print("Rendering Circle")

class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def render(self):
        for graphic in self.graphics:
            graphic.render()

# Usage
circle1 = Circle()
circle2 = Circle()

group = CompositeGraphic()
group.add(circle1)
group.add(circle2)
group.render()  # Rendering Circle\nRendering Circle
