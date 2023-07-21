class DiningExperienceManager:
    MENU = {
        "Burger": 5,
        "Pizza": 5,
        "Pasta": 5,
        "Salad": 5,
        "Ice Cream": 5,
        "Big Mac1": 10,
        "Big Mac 2": 12,
    }

    SPECIAL_MEALS_SURCHARGE = 0.05
    QUANTITY_DISCOUNTS = {6: 0.1, 11: 0.2}
    TOTAL_COST_DISCOUNTS = {51: 10, 101: 25}

    def __init__(self):
        self.order = {}

    def display_menu(self):
        print("MENU:")
        for item, price in self.MENU.items():
            print(f"{item}: ${price}")

    def get_valid_quantity(self):
        while True:
            quantity = input("Enter quantity (positive integer greater than zero): ")
            if quantity.isdigit() and int(quantity) > 0:
                return int(quantity)
            print("Invalid input. Please enter a positive integer greater than zero.")

    def take_order(self):
        print("Welcome to our Dining Experience Manager!")
        self.display_menu()
        print("Enter 'done' when you have finished your order.")
        while True:
            item = input("\nEnter the name of the meal you want to order: ")
            if item.lower() == 'done':
                break
            elif item in self.MENU:
                quantity = self.get_valid_quantity()
                self.order[item] = self.order.get(item, 0) + quantity
            else:
                print("Invalid meal selection. Please choose from the menu.")

    def apply_quantity_discount(self, price, quantity):
        for threshold, discount in self.QUANTITY_DISCOUNTS.items():
            if quantity > threshold:
                return price * (1 - discount)
        return price

    def calculate_total_cost(self):
        total_cost = 0
        for item, quantity in self.order.items():
            price = self.MENU[item]
            if item.startswith("Big Mac"):
                price *= 1 + self.SPECIAL_MEALS_SURCHARGE
            price = self.apply_quantity_discount(price, quantity)
            total_cost += price * quantity

        for threshold, discount in self.TOTAL_COST_DISCOUNTS.items():
            if total_cost > threshold:
                total_cost -= discount

        return total_cost

    def run(self):
        self.take_order()
        if not self.order:
            print("Order canceled. No items selected.")
            return -1

        total_cost = self.calculate_total_cost()
        if total_cost <= 0:
            print("Invalid order or calculation error. Please check your input.")
            return -1

        print("\nOrder Summary:")
        for item, quantity in self.order.items():
            print(f"{item} x{quantity}")
        print(f"Total Cost: ${total_cost:.2f}")
        return int(total_cost)


if __name__ == "__main__":
    dining_manager = DiningExperienceManager()
    total_cost = dining_manager.run()
    if total_cost != -1:
        print(f"Thank you for dining with us! Your total cost is ${total_cost}.")
