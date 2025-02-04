phone_book = {}

def add_contact(name, number):
    phone_book[name] = number
    print("ok!")

def search_contact(name):
    if name in phone_book:
        print(phone_book[name])
    else:
        print("no number")

def main():
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == '1':
            name = input("name: ")
            search_contact(name)
        elif command == '2':
            name = input("name: ")
            number = input("number: ")
            add_contact(name, number)
        elif command == '3':
            print("quitting...")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()