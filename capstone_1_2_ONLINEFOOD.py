class FoodDeliverySystem:
    def __init__(self):
        self.menu = {
            "Pizza": (300, "Fast Food"),
            "Burger": (150, "Fast Food"),
            "Pasta": (200, "Italian"),
            "Salad": (100, "Healthy")
        }
        self.orders = []
        self.unique_customers = set()
        self.order_id = 1

    def display_menu(self):
        print("\nMenu:")
        for item, (price, category) in self.menu.items():
            print(f"{item}: Rs.{price} ({category})")

    def place_order(self, customer_name, items):
        total_bill = sum(self.menu[item][0] for item in items if item in self.menu)
        self.orders.append((self.order_id, customer_name, items, total_bill))
        self.unique_customers.add(customer_name)
        print(f"Order placed! Order ID: {self.order_id}, Total Bill: Rs.{total_bill}")
        self.order_id += 1

    def total_revenue(self):
        revenue = sum(order[3] for order in self.orders)
        print(f"Total Revenue: Rs.{revenue}")

    def unique_customers_list(self):
        print("Unique Customers:", self.unique_customers)

# Example Usage
fds = FoodDeliverySystem()
fds.display_menu()
fds.place_order("Alice", ["Pizza", "Burger"])
fds.place_order("Bob", ["Pasta", "Salad"])
fds.total_revenue()
fds.unique_customers_list()
