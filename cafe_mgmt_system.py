# Cafe Management System using Dictionary

menu = {
    1: {"name": "Coffee", "price": 2.50},
    2: {"name": "Tea", "price": 1.50},
    3: {"name": "Sandwich", "price": 3.00}
}

ADMIN_PASSWORD = "araartrr"

# Function to add an item to the menu
def add_item(item_id, name, price):
    menu[item_id] = {"name": name, "price": price}
    print(f"Added {name} with price ${price:.2f} to the menu.")

# Function to delete an item from the menu
def delete_item(item_id):
    if item_id in menu:
        item = menu.pop(item_id)
        print(f"Deleted {item['name']} from the menu.")
    else:
        print(f"Item with ID {item_id} not found.")

# Function to update the price of an item
def update_price(item_id, new_price):
    if item_id in menu:
        menu[item_id]['price'] = new_price
        print(f"Updated price of {menu[item_id]['name']} to ${new_price:.2f}.")
    else:
        print(f"Item with ID {item_id} not found.")

# Function to view the menu
def view_menu():
    print("Menu:")
    for item_id, item_info in menu.items():
        print(f"{item_id}. {item_info['name']} - ${item_info['price']:.2f}")

# Function to place an order
def place_order():
    order_items = []
    while True:
        item_id = int(input("Enter item ID to order (0 to finish): "))
        if item_id == 0:
            break
        elif item_id in menu:
            order_items.append(item_id)
        else:
            print("Invalid item ID.")
    if order_items:
        total = 0
        print("\nOrder details:")
        for item_id in order_items:
            item = menu[item_id]
            print(f"{item['name']} - ${item['price']:.2f}")
            total += item['price']
        print(f"Total amount: ${total:.2f}")
        
        while True:
            paid_amount = float(input("Enter the amount to be paid: $"))
            if paid_amount == total:
                print("Thank you for ordering! Have a nice day. Please visit again.")
                break
            else:
                print("Wrong input. Please enter the correct amount.")
    else:
        print("No items ordered.")

# Function to handle admin tasks
def admin_tasks():
    while True:
        print("\nAdmin Menu:")
        print("1. Add item")
        print("2. Delete item")
        print("3. Update price")
        print("4. View menu")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            add_item(item_id, name, price)
        elif choice == 2:
            item_id = int(input("Enter item ID to delete: "))
            delete_item(item_id)
        elif choice == 3:
            item_id = int(input("Enter item ID to update price: "))
            new_price = float(input("Enter new price: "))
            update_price(item_id, new_price)
        elif choice == 4:
            view_menu()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    print("Welcome to AARR Cafe!")
    role = input("Are you an Admin or a Customer? ").strip().lower()
    if role == "admin":
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            admin_tasks()
        else:
            print("Incorrect password. Access denied.")
    elif role == "customer":
        view_menu()
        place_order()
    else:
        print("Invalid role. Please enter 'Admin' or 'Customer'.")

# Run the main function
if __name__ == "__main__":
    main()

