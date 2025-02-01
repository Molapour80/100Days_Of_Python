import json
import os

class Inventory:
    def __init__(self):
        self.items = {}
        self.load_inventory()

    def load_inventory(self):
        if os.path.exists('inventory.json'):
            with open('inventory.json', 'r') as file:
                self.items = json.load(file)

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        self.save_inventory()
        print(f"Added {quantity} of {name}. Current quantity: {self.items[name]}")

    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name] >= quantity:
                self.items[name] -= quantity
                if self.items[name] == 0:
                    del self.items[name]
                self.save_inventory()
                print(f"Removed {quantity} of {name}. Current quantity: {self.items.get(name, 0)}")
            else:
                print("Not enough quantity to remove.")
        else:
            print("Item not found.")

    def show_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for name, quantity in self.items.items():
                print(f"{name}: {quantity}")

    def search_item(self, name):
        if name in self.items:
            print(f"{name} is in inventory with quantity: {self.items[name]}")
        else:
            print(f"{name} not found in inventory.")

def main():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Show Inventory")
        print("4. Search Item")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(name, quantity)
        elif choice == '3':
            inventory.show_inventory()
        elif choice == '4':
            name = input("Enter item name to search: ")
            inventory.search_item(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        elif choice == " ":
            continue
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()