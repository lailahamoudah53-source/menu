class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_info(self):
        print("Name:", self.name)
        print("Phone:", self.phone)


# Customer class (Inheritance from person)
class Customer(Person):
    def __init__(self, name, phone, customer_id):
        super().__init__(name, phone)
        self.customer_id = customer_id

    def display_info(self):
        super().display_info()
        print("Customer ID:", self.customer_id)


# Product class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price:", self.price)


# Order class
class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity

    def display_info(self):
        print("Order ID:", self.order_id)
        self.product.display_info()
        print("Quantity:", self.quantity)
        print("Total Price:", self.calculate_total())


# Main (Test)
customer1 = Customer("Laila", "0591234567", 1)
product1 = Product(101, "Laptop", 3500)
order1 = Order(5001, product1, 2)

print("Customer Info:")
customer1.display_info()

print("\nOrder Info:")
order1.display_info()
