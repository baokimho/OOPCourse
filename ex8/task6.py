class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class PricingCalculator:
    def __init__(self, discount=False, tax=False):
        self.discount = discount
        self.tax = tax

    def calculate(self, items):
        total = sum(item.total_price() for item in items)
        if self.discount:
            total *= 0.9
        if self.tax:
            total *= 1.2
        return total

class Order:
    def __init__(self, items, calculator: PricingCalculator):
        self.items = items
        self.calculator = calculator

    def total(self):
        return self.calculator.calculate(self.items)

    def print_order(self):
        print("Items:")
        for item in self.items:
            print(f"  {item.name} x {item.quantity} @ {item.price} = {item.total_price()}")
        print(f"Discount applied: {self.calculator.discount}")
        print(f"Tax applied: {self.calculator.tax}")
        print(f"Total: {self.total()}")
