
# Person

class Person:
    def __init__(self, name: str, number: str):
        self._name = name
        self._number = number

class Customer(Person):
    def __init__(self, name: str, number: str):
        super().__init__(name, number)
        self._orders = []
    
    def overview(self):
        print(f"\n Customer: {self._name}")
        total = 0
        
        for order in self._orders:
            print("Order:")
            order.show()
            total += order.total()
        
        print(f"TOTAL BOUGHT: {total:.2f} kr")

class Producer(Person):
    def __init__(self, name: str, number: str):
        super().__init__(name, number)

        self._products = []
        self._customers = []
        self._orders = []

    # ---------- REGISTER ----------
    def add_product(self, product):
        self._products.append(product)

    def add_customer(self, customer):
        self._customers.append(customer)

    def add_order(self, order):
        self._orders.append(order)
        order._customer._orders.append(order)

    # ---------- CREATE ORDER (MAIN FUNCTION) ----------
    def create_order(self, customer):
        order = Order(customer)
        self.add_order(order)
        return order

    # ---------- REPORTS ----------
    def product_summary(self):
        print("\nPRODUCT SUMMARY:")
        for product in self._products:
            print(f"- {product._name}: {product.total_sold()} kg sold")

    def customer_summary(self):
        print("\nCUSTOMERS:")
        for customer in self._customers:
            print(f"- {customer._name}")

    def total_revenue(self):
        return sum(order.total() for order in self._orders)

    def full_report(self):
        print("\n===== BARLIND GÅRD REPORT =====")

        print("\nFarm owner:", self._name)

        self.customer_summary()
        self.product_summary()

        print("\nTOTAL REVENUE:")
        print(f"{self.total_revenue():.2f} kr")

# Products

class Product:
    def __init__(self, name: str, description: str, kilo_price: float):
        self._name = name
        self._description = description
        self._kilo_price = kilo_price
        self._sold = 0
        
    def add_sold(self, quantity: float):
        self._sold += quantity
    
    def total_sold(self):
        return self._sold

class Apple(Product):
    def __init__(self, name, description, kilo_price, color: str):
        super().__init__(name, description, kilo_price)
        self._color = color


class Flour(Product):
    def __init__(self, name, description, kilo_price, BB_date: str):
        super().__init__(name, description, kilo_price)
        self._BB_date = BB_date

# Orders

class OrderItem:
    def __init__(self, product, quantity: float):
        self._product = product
        self._quantity = quantity
    
    def total_price(self):
        return self._product._kilo_price * self._quantity

class Order:
    def __init__(self, customer):
        self._customer = customer
        self._items = []
    
    def add_item(self, product, quantity: float):
        self._items.append(OrderItem(product, quantity))
        product.add_sold(quantity)
    
    def total(self):
        return sum(item.total_price() for item in self._items)
    
    def show(self):
        print(f"\nOrder for {self._customer._name}")
        for item in self._items:
            print(f"- {item._quantity} kg {item._product._name}")
        print(f"Total: {self.total():.2f} kr")