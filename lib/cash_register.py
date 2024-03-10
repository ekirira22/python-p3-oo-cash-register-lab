import ipdb

class CashRegister:
    total = 0
    items = []
    last_transaction = {}

    def __init__(self, discount=0):
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = {'title': title, 'price': price * quantity, 'quantity': quantity}
        self.items.append(title)
        return self.items

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            self.apply_discount_when_no_discount()

    def apply_discount_when_no_discount(self):
        print("There is no discount to apply.")

    def void_last_transaction(self):
        title = self.last_transaction['title']
        price = self.last_transaction['price']
        quantity = self.last_transaction['quantity']

        if quantity > 1:
            pass

        self.total -= price
        self.items.remove(title)


# new_register = CashRegister()
# new_register.add_item("eggs", 1.99, 2)
# new_register.add_item("tomato", 1.76, 3)
# print(new_register.last_transaction)












