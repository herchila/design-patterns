class Coffee:
    def get_cost(self):
        raise NotImplementedError

    def get_ingredients(self):
        raise NotImplementedError


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 2

    def get_ingredients(self):
        return 'Coffee'


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.decorated_coffee = coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class WithMilk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.5

    def get_ingredients(self):
        return super().get_ingredients() + ', Milk'


class WithSugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 0.25

    def get_ingredients(self):
        return super().get_ingredients() + ', Sugar'


# Usage
my_coffee = SimpleCoffee()
print(f"Cost: {my_coffee.get_cost()}; Ingredients: {my_coffee.get_ingredients()}")

my_coffee = WithMilk(my_coffee)
print(f"Cost: {my_coffee.get_cost()}; Ingredients: {my_coffee.get_ingredients()}")

my_coffee = WithSugar(my_coffee)
print(f"Cost: {my_coffee.get_cost()}; Ingredients: {my_coffee.get_ingredients()}")
