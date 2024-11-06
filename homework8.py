def main():
    # Create a dictionary
    contacts = {
        'Alice': '555-1234',
        'Bob': '555-5678',
        'Charlie': '555-8765'
    }
    # Accessing Dictionary Elements
    print(contacts['Bob'])
    if 'David' in contacts:
        print("David located!")
    else:
        print("No David to be found...\n")
    
    # Updating an Removing Items
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    while name in contacts:
        print("Name is already a key in contacts.\n")
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
    contacts[name] = phone_number
    print(f"Contact list after adding {name} and {phone_number}:", end="")
    print(contacts)
    del contacts["Charlie"]
    print(f"Contact list after deleting Charlie:", end="")
    print(contacts)
    contacts["Alice"] = '555-9999'
    print(f"Contact list after modifying Alice:", end="")
    print(contacts)
    
    # Iterating Over a Dictionary
    dic_to_set = set(contacts.keys())
    print(f"\nDictionary to set: {dic_to_set}\n")
    print_key_val(contacts)

# Function that takes a dictionary and prints key: val
def print_key_val(dic):
    for key in dic:
        print(f"{key}: {dic[key]}\n")

if __name__ == "__main__":
    main()






