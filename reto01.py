from datetime import datetime

inventory = []

def validate(name):
    flag = True
    for item in inventory:
        if item.get("name") == name:
            flag = False
    return flag


def add_new_item():
    name = input("Item Name: ")
    if name.strip() != "" and validate(name):
        quantity = int(input("Amount: "))
        price = float(input("Price: "))
        type = input("Type: ")
        size = input("Size: ")
        date = datetime.today().strftime('%Y-%m-%d')
        item = {
            "id": len(inventory) + 1,
            "name": name,
            "quantity": quantity,
            "price": price,
            "type": type,
            "size": size,
            "last_update": date
        }
        inventory.append(item)
        print(f"Item: {name}, was added successfully.")
    else:
        print("This item is no longer available")

def update_item():
    name = input("Item Name: ")
    for item in inventory:
        if item.get("name") == name:
            item["quantity"] = input("New Amount: ")
            item["price"] = input("New Price: ")
            item["type"] = input("New Type: ")
            item["size"] = input("New Size: ")
            item["last_update"] = datetime.today().strftime('%Y-%m-%d')
            print(f"Item: {name}, was updated successfully.")

def find_item():
    option = int(
        input("Find by: \n1.Name\n2.Size\n3.Type\n4.Date\nSelect an option:")
    )
    options = {
        1: lambda: find_by_name(),
        2: lambda: find_by_size(),
        3: lambda: find_by_type(),
        4: lambda: find_by_date(),
    }
    options.get(option, lambda: print("Invalid Option"))()


def find_by_name():
    name = input("Name: ")
    filtered_items = list(
        filter(
            lambda item: name.lower() in item.get("name").lower(),
            inventory,
        )
    )
    print("Items found: ")
    print_items(filtered_items)

def find_by_size():
    size = input("Size: ")
    filtered_items = list(
        filter(
            lambda item: size.lower() in item.get("size").lower(), inventory
        )
    )
    print("Items found: ")
    print_items(filtered_items)


def find_by_type():
    type = input("Type: ")
    filtered_items = list(
        filter(
            lambda item: type.lower() in item.get("type").lower(), inventory
        )
    )
    print("Items found: ")
    print_items(filtered_items)

def find_by_date():
    date = input("Date: ")
    filtered_items = list(
        filter(
            lambda item: date.lower() in item.get("last_update").lower(), inventory
        )
    )
    print("Items found: ")
    print_items(filtered_items)


def order_items():
    option = int(
        input("Order by: \n1.Name\n2.Size\n3.Type\nSelect and option:")
    )
    options = {
        1: lambda: sorted(inventory, key=lambda item: item.get("name")),
        2: lambda: sorted(inventory, key=lambda item: item.get("size")),
        3: lambda: sorted(inventory, key=lambda item: item.get("type")),
    }
    data = options.get(option, lambda: [])()
    print_items(data)


def delete_item():
    name = input("Name: ")
    ind = -1
    for index, item in enumerate(inventory):
        if name == item.get("name"):
            inventory.pop(index)
            print("Deleted successfully. ")


def decrease_item():
    name = input("Name: ")
    quantity = int(input("Amount to decrease: "))
    for item in inventory:
        if name == item.get("name"):
            item["quantity"] = item.get("quantity") - quantity
            print("Successful operation.")


def increase_item():
    name = input("Name: ")
    quantity = int(input("Amount to decrease: "))
    for item in inventory:
        if name == item.get("name"):
            item["quantity"] = item.get("quantity") + quantity
            print("Successful operation.")


def get_total():
    total = 0
    for item in inventory:
        total += item.get("quantity")
    print(f"Total: {total} items.")


def print_items(items):
    print(
        "| {:10} | {:15} | {:10} | {:10} | {:15} | {:10} | {:10}".format(
            "ID", "NAME", "TYPE", "SIZE", "QUANTITY", "PRICE", "DATE"
        )
    )
    for item in items:
        print(
            "| {:10} | {:15} | {:11}| {:10} | {:15} | {:10} | {:10}".format(
                item.get("id"),
                item.get("name"),
                item.get("type"),
                item.get("size"),
                item.get("quantity"),
                item.get("price"),
                item.get("last_update"),
            )
        )
        print("\n")
        
def report_txt():
    separator = "+" + "-" * 100 + "+"
    file = open("inventory_report.txt","w")
    file.write("Control")
    file.write(separator)
    file.write("\n")
    file.write( "| {:10} | {:15} | {:10} | {:10} | {:10} | {:10} | {:10}".format(
            "ID", "NAME", "TYPE", "SIZE", "QUANTITY", "PRICE", "DATE"
        ))
    file.write("\n")
    file.write(separator)
    file.write("\n")
    for item in inventory:
        file.write("| {:10} | {:15} | {:11}| {:10} | {:10} | {:10} | {:10}".format(
                item.get("id"),
                item.get("name"),
                item.get("type"),
                item.get("size"),
                item.get("quantity"),
                item.get("price"),
                item.get("last_update"),
            ))
        file.write("\n")
    file.write(separator)
    file.close()


def get_message_choice(option):
    msg = "The option was not found."
    if option == 11:
        msg = "You have exited the inventory control."
    return msg


def main_menu():
    choice = 0
    while choice != 11:
        print("\n------- INVENTORY -------")
        print("1. Add new Item.")
        print("2. Update Item.")
        print("3. Find Item.")
        print("4. Order Items.")
        print("5. Delete Items.")
        print("6. Decrease Items.")
        print("7. Increase Items")
        print("8. Calculate Total")
        print("9. Show Inventory.")
        print("10. Generate report.")
        print("11. Exit")
        choice = int(input("Select an option: "))

        options = {
            1: lambda: add_new_item(),
            2: lambda: update_item(),
            3: lambda: find_item(),
            4: lambda: order_items(),
            5: lambda: delete_item(),
            6: lambda: decrease_item(),
            7: lambda: increase_item(),
            8: lambda: get_total(),
            9: lambda: print_items(inventory),
            10: lambda: report_txt()
        }
        options.get(choice, lambda: print(get_message_choice(choice)))()


main_menu()
