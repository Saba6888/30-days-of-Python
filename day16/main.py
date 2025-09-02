shopping_list = []

def show_menu():
    print("\nShopping List Menu:")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("\nYour shopping list is empty!")

def add_item():
    item = input("\nEnter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f'"{item}" has been added to your shopping list.')
    else:
        print("Item cannot be empty!")

def remove_item():
    if shopping_list:
        try:
            view_list()
            item_no = int(input("\nEnter the number of the item to remove: "))
            if 1 <= item_no <= len(shopping_list):
                removed_item = shopping_list.pop(item_no - 1)
                print(f'"{removed_item}" has been removed from your shopping list.')
            else:
                print("Invalid item number!")
        except ValueError:
            print("Please enter a valid number!")
    else:
        print("\nYour shopping list is empty!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == '1':
            view_list()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            print("\nExiting the Shopping List Application. Happy Shopping!")
            break
        else:
            print("Invalid choice! Please select from the menu.")

if __name__ == "__main__":
    main()
