class Supplier:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Supplier: {self.name}"

class Product:
    def __init__(self, name, quantity, supplier):
        self.name = name
        self.quantity = quantity
        self.supplier = supplier

    def restock(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity}) - {self.supplier}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_inventory(self):
        for product in self.products:
            print(product)

supplier1 = Supplier("Acme Inc.")
product1 = Product("Widget", 10, supplier1)
product2 = Product("Gadget", 5, supplier1)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
product1.restock(20)
inventory.print_inventory()