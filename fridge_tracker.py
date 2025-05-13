import shelve

def add_item(item):
    with shelve.open('fridge') as fridge:
        items = fridge.get('items', [])
        items.append(item)
        fridge['items'] = items
        print(f"Added '{item}' to the fridge.")

def list_items():
    with shelve.open('fridge') as fridge:
        items = fridge.get('items', [])
        if items:
            print("Items in the fridge:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
        else:
            print("The fridge is empty.")

def remove_item(item):
    with shelve.open('fridge') as fridge:
        items = fridge.get('items', [])
        if item in items:
            items.remove(item)
            fridge['items'] = items
            print(f"Removed '{item}' from the fridge.")
        else:
            print(f"{item} not found in the fridge.")

# --- Simple command interface ---
while True:
    print("\nChoose an action:")
    print("1. Add item")
    print("2. List items")
    print("3. Remove item")
    print("4. Exit")
    choice = input("Your choice: \n").strip()

    if choice == '1':
        item = input("Enter item to add: ").strip()
        add_item(item)

    elif choice == '2':
        list_items()

    elif choice == '3':
        list_items()
        item = input("Enter item to remove: ").strip()
        remove_item(item)

    elif choice == '4':
        print(" Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
