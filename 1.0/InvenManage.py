from datetime import datetime
inventory = {}

def add_item(name, category, quantity, price, expiry_date):
    if name in inventory:
        print(f"Item '{name}' already exists. Use 'update_item' to change details.")
    else:
        try:
            expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
            inventory[name] = {
                "category": category,
                "quantity": quantity,
                "price": price,
                "expiry_date": expiry
            }
            print(f"Item '{name}' added to inventory.")
        except ValueError:
            print("Invalid expiry date format. Use YYYY-MM-DD.")

def update_item(name, category=None, quantity=None, price=None, expiry_date=None):
    if name in inventory:
        if category is not None:
            inventory[name]["category"] = category
        if quantity is not None:
            inventory[name]["quantity"] = quantity
        if price is not None:
            inventory[name]["price"] = price
        if expiry_date is not None:
            try:
                expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
                inventory[name]["expiry_date"] = expiry
            except ValueError:
                print("Invalid expiry date format. Use YYYY-MM-DD.")
        print(f"Item '{name}' updated.")
    else:
        print(f"Item '{name}' does not exist. Use 'add_item' to add the item.")

def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from inventory.")
    else:
        print(f"Item '{name}' does not exist.")

def view_inventory():
    if inventory:
        print("Current Inventory:")
        for name, details in inventory.items():
            expiry_str = details['expiry_date'].strftime("%Y-%m-%d")
            print(f"Item: {name}, Category: {details['category']}, Quantity: {details['quantity']}, Price: ${details['price']}, Expiry Date: {expiry_str}")
    else:
        print("Inventory is empty.")

def view_item(name):
    if name in inventory:
        details = inventory[name]
        expiry_str = details['expiry_date'].strftime("%Y-%m-%d")
        print(f"Item: {name}, Category: {details['category']}, Quantity: {details['quantity']}, Price: ${details['price']}, Expiry Date: {expiry_str}")
    else:
        print(f"Item '{name}' not found in inventory.")

def check_expired_items():
    print("\nExpired Items:")
    today = datetime.today()
    expired_items = False
    for name, details in inventory.items():
        if details['expiry_date'] < today:
            expiry_str = details['expiry_date'].strftime("%Y-%m-%d")
            print(f"Item: {name}, Expired on: {expiry_str}")
            expired_items = True
    if not expired_items:
        print("No expired items found.")

def main_menu():
    while True:
        print("\nWelcome to the DevOps Inventory")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. View Item Details")
        print("6. Check Expired Items")
        print("7. Exit")
        
        choice = input("Please select an option (1-7): ")
        
        if choice == "1":
            name = input("Enter item name: ")
            category = input("Enter item category: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            expiry_date = input("Enter item expiry date (YYYY-MM-DD): ")
            add_item(name, category, quantity, price, expiry_date)
        elif choice == "2":
            name = input("Enter item name to update: ")
            category = input("Enter new category (or leave blank to skip): ")
            quantity = input("Enter new quantity (or leave blank to skip): ")
            price = input("Enter new price (or leave blank to skip): ")
            expiry_date = input("Enter new expiry date (YYYY-MM-DD) (or leave blank to skip): ")
            update_item(
                name,
                category if category else None,
                int(quantity) if quantity else None,
                float(price) if price else None,
                expiry_date if expiry_date else None
            )
        elif choice == "3":
            name = input("Enter item name to remove: ")
            remove_item(name)
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            name = input("Enter item name to view details: ")
            view_item(name)
        elif choice == "6":
            check_expired_items()
        elif choice == "7":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
