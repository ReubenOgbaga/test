# meal_ordering_app.py

import json

# Sample menu data for demonstration
MENU = {
    "Burger": 5.99,
    "Ice-cream": 1.25,
    "Pizza": 8.99,
    "Salad": 4.50,
    "Soda": 1.25,
    "Fries": 2.00,
    "Chicken": 8.00,
    "Cerelac": 5.25,
    "Sharwama": 5.50
}

# Initialize an empty cart
cart = {}

def display_menu():
    """Display the available menu items and prices."""
    print("Menu:")
    for item, price in MENU.items():
        print(f"{item}: ${price:.2f}")
    print("\n")

def add_to_cart(item, quantity=1):
    """Add a specified quantity of an item to the cart."""
    if item in MENU:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} x {item} to cart.")
    else:
        print(f"Item '{item}' not found in the menu.")

def view_cart():
    """Display the contents of the cart with the quantity and individual prices."""
    print("\nYour Cart:")
    if not cart:
        print("Cart is empty.")
        return
    for item, quantity in cart.items():
        print(f"{item} x {quantity}: ${MENU[item] * quantity:.2f}")
    print("\n")

def calculate_total():
    """Calculate the total cost of items in the cart."""
    total = sum(MENU[item] * quantity for item, quantity in cart.items())
    return round(total, 2)

def checkout():
    """Simulate checkout process and display total."""
    if not cart:
        print("Your cart is empty. Add items to your cart before checking out.")
        return
    total = calculate_total()
    print(f"Your total is: ${total:.2f}")
    print("Thank you for your order!")

def reset_cart():
    """Reset the cart to empty."""
    global cart
    cart = {}
    print("Cart has been reset.")

def take_user_order():
    """Prompt user for items to add to cart with quantity."""
    while True:
        display_menu()
        item = input("Enter the item you want to add to the cart (or type 'done' to finish): ").title()
        if item.lower() == 'done':
            break
        if item not in MENU:
            print("This item is not on the menu. Please choose a valid item.")
            continue
        try:
            quantity = int(input(f"Enter the quantity of {item} you want to add: "))
            if quantity <= 0:
                print("Please enter a quantity greater than 0.")
                continue
            add_to_cart(item, quantity)
            view_cart()
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")

# Example usage of the functions (these could be modified for more advanced CLI or GUI integration)
if __name__ == "__main__":
    take_user_order()
    print(f"Total: ${calculate_total()}")
    checkout()
