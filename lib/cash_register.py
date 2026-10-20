#!/usr/bin/env python3


class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction = 0

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.items.extend([title] * quantity)
        self._last_transaction = amount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (1 - self.discount / 100)

        display = int(self.total) if self.total == int(self.total) else self.total
        print(f"After the discount, the total comes to ${display}.")

    def void_last_transaction(self):
        self.total -= self._last_transaction
        self._last_transaction = 0
