def display_menu():
    print("\nContact Book Menu:")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    choice=input("Enter your choice between 1 to 5:")
    return choice

def add_contact(contacts):
    phone=input("Enter the contact number: ")
    name=input("Enter the name to be saved: ")
    email=input("enter email of the person: ")
    contact={'phone':phone, 'name':name, 'email':email}
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contact(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        for i, contact in enumerate(contacts,start=1):
            print(f"{i}.{contact['name']}-phone:{contact['phone']}-email:{contact['email']}")

def search_contact(contacts):
    search_name=input("Enter the contact name: ").lower()
    found_contacts=[contact for contact in contact if contact['name'].lower()==search_name]

    if found_contacts:
        for contact in found_contacts:
            print(f"Found: {contact['name']} - Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contact found with the name '{search_name}'.")
    
def delete_contact(contacts):
    delete_name=input("Enter the contact name to be deleted: ")
    for contact in contacts:
        if contact['name'].lower()==delete_name:
            contacts.remove(contact)
            print("Contact {delete_name} successfully deletd!")
            return
    print("Cannot find contact {delete_name}")

def main():
    contacts=[]
    while True:
        choice = display_menu()
        if choice=='1':
            add_contact(contacts)
        elif choice=='2':
            view_contact(contacts)
        elif choice=='3':
            search_contact(contacts)
        elif choice=='4':
            delete_contact(contacts)
        elif choice=='5':
            print("Exiting contact book!")
            break
if __name__=="__main__":
    main()
