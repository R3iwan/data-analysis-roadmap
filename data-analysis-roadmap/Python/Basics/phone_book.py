phone_book = {}

while True:
    command = input("Please write a command you want to use:\n1)add \n2)find \n3)delete \n4)show all \n5)exit")
    if command.lower() == 'add':
        name = input("Please write your name:\n")
        if name.lower() in phone_book.keys():
            print("Name already exists")
        phone = input("Please write your phone number")
        phone_book[name] = phone

    elif command.lower() == 'find':
        name_to_find = input("Please write a name for finding phone")
        contact_phone = phone_book.get(name_to_find.lower())
        if contact_phone:
            print(f"Phone number for '{name_to_find}': {contact_phone}")
        else:
            print(f"Contact '{name_to_find}' not found.")

    elif command.lower() == 'delete':
        name_to_delete = input("Enter name to delete: ")
        if phone_book.pop(name_to_delete.lower(), None):
             print(f"Contact '{name_to_delete}' deleted successfully!")
        else:
            print(f"Contact '{name_to_delete}' not found.")

    elif command.lower() == 'show all':
        print("--- Your Tasks ---")
        if not phone_book:
            print("You don't have any tasks")
        else:
            for name, phone in phone_book.items():
                print(f"- {name.title()}: {phone}")
        print("--------------------\n")    

    elif command.lower() == 'exit':
        break