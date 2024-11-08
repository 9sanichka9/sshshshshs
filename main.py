class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact_info}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total_price = 0.0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.calculate_total()

    def calculate_total(self):
        self.total_price = sum(item.price for item in self.items)

    def __str__(self):
        item_list = "\n".join(str(item) for item in self.items)
        return (f"Order for {self.customer}\n"
                f"Items:\n{item_list}\n"
                f"Total: ${self.total_price:.2f}")


if __name__ == "__main__":
    item1 = Item("Coffee", 2.5)
    item2 = Item("Sandwich", 5.0)
    item3 = Item("Cake", 3.0)

    customer = Customer("John Doe", "john@example.com")
    order = Order(customer)

    order.add_item(item1)
    order.add_item(item2)
    order.add_item(item3)

    print(order)

    order.remove_item(item2)

    print("nAfter removing Sandwich:")
    print(order)
