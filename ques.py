import os

inventory = {}
file_name = "vend.dat"
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            item, quantity = line.strip().split(',')
            inventory[item] = int(quantity)

def dispense_item(item):
    if item in inventory and inventory[item] > 0:
        print(f"Dispensing {item}")
        inventory[item] -= 1
        update_inventory()
    else:
        print("Item not available")

def update_inventory():
    with open(file_name, 'w') as file:
        for item, quantity in inventory.items():
            file.write(f"{item},{quantity}\n")

def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

while True:
    choice = input("Enter the number of the item you want to purchase (1-25), or 'q' to quit: ")
    if choice.lower() == 'q':
        break
    try:
        choice = int(choice)
        if choice < 1 or choice > 25:
            print("Invalid input. Please enter a number between 1 and 25.")
            continue
        item = f"Item {choice}"
        dispense_item(item)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 25 or 'q' to quit.")

display_inventory()
