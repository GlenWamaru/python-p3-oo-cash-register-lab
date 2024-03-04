class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.items = []
        self.total = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append({"title": title, "price": price})
            self.total += price

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item["price"]

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}.\n"
        else:
            return "There is no discount to apply.\n"

    def items_list(self):
        return [item["title"] for item in self.items]

    def items_with_multiples(self):
        return [item["title"] for item in self.items]

    def reset_total(self):
        self.total = 0
