from classes import (Producer, Apple, Flour, Customer)

class FarmSystem:
    def __init__(self):
        self.farm = Producer("Magne Auke", "44554455")
        self.setup_demo_data()

    # ---------------- DEMO DATA ----------------
    def setup_demo_data(self):
        self.farm.add_product(Apple("Granny Smith", "Sour apple", 40, "green"))
        self.farm.add_product(Apple("Aroma", "Sweet apple", 42, "red"))
        self.farm.add_product(Flour("Wheat Flour", "Fine flour", 30, "2026-10-10"))

    # ---------------- MAIN MENU ----------------
    def run(self):
        while True:
            print("\n===== FARM SYSTEM MENU =====")
            print("1. Show products")
            print("2. Add customer")
            print("3. Add product")
            print("4. Create order")
            print("5. OVERVIEW REPORT")
            print("6. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.show_products()

            elif choice == "2":
                self.add_customer()

            elif choice == "3":
                self.add_product()
                
            elif choice == "4":
                self.create_order()
            
            elif choice == "5":
                self.overview()

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice!")

    # ---------------- BASIC FUNCTIONS ----------------
    def show_products(self):
        print("\n--- PRODUCTS ---")
        for p in self.farm._products:
            print(f"- {p._name} ({p._kilo_price} kr/kg)")

    def add_customer(self):
        name = input("Customer name: ")
        number = input("Phone number: ")

        customer = Customer(name, number)
        self.farm.add_customer(customer)

        print("Customer added!")
    
    
    def add_product(self):
        print("\n--- ADD PRODUCT ---")
        print("1. Apple")
        print("2. Flour")

        choice = input("Choose product type: ")

        name = input("Product name: ")
        description = input("Description: ")
        price = float(input("Price per kg: "))

        if choice == "1":
            color = input("Color: ")
            product = Apple(name, description, price, color)

        elif choice == "2":
            bb_date = input("Best before date: ")
            product = Flour(name, description, price, bb_date)

        else:
            print("Invalid product type!")
            return

        self.farm.add_product(product)
        print(f"{name} added successfully!")

    def create_order(self):
        if not self.farm._customers:
            print("No customers available!")
            return

        print("\nSelect customer:")
        for i, c in enumerate(self.farm._customers):
            print(f"{i + 1}. {c._name}")

        c_index = int(input("Choose customer: ")) - 1
        customer = self.farm._customers[c_index]

        order = self.farm.create_order(customer)

        while True:
            print("\nSelect product (x to finish):")
            for i, p in enumerate(self.farm._products):
                print(f"{i + 1}. {p._name}")

            choice = input("Product: ")

            if choice.lower() == "x":
                break

            p_index = int(choice) - 1
            product = self.farm._products[p_index]

            qty = float(input("Quantity (kg): "))
            order.add_item(product, qty)

        print("Order completed!")

    # ---------------- Overview (IMPORTANT PART) ----------------
    def overview(self):
        print("\n===== OVERVIEW REPORT =====")

        # 1. Producer + products
        print("\n--- PRODUCER & PRODUCTS ---")
        print(f"Farm owner: {self.farm._name}")

        for p in self.farm._products:
            print(f"{p._name} → {p.total_sold()} kg sold")

        # 2. Customers + what they bought
        print("\n--- CUSTOMER PURCHASES ---")
        for c in self.farm._customers:
            print(f"\nCustomer: {c._name}")

            if not c._orders:
                print("No orders")
                continue

            total = 0
            for order in c._orders:
                for item in order._items:
                    print(f"- {item._quantity} kg {item._product._name}")
                total += order.total()

            print(f"TOTAL SPENT: {total:.2f} kr")

        # 3. Total revenue
        print("\n--- TOTAL REVENUE ---")
        print(f"{self.farm.total_revenue():.2f} kr")

def main():
    system = FarmSystem()
    system.run()

if __name__ == "__main__":
    main()