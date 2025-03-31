class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def add_address(self, address):
        if address == self.__address:
            print("The new address should be different")
            return False
        else:
            self.__address = address
            return True

    def add_number(self, number):
        if number in self.__numbers:
            return False
        else:
            self.__numbers.append(number)
            return True


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name, number):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_numbers(self, name):
        if name not in self.__persons:
            return "number unknown"
        return self.__persons[name].numbers()

    def add_address(self, name, address):
        if name not in self.__persons:
            print("The name doesn't exist")
            return False
        return self.__persons[name].add_address(address)  # Return the result

    def get_entry(self, name):
        if name in self.__persons:
            person = self.__persons[name]
            numbers = person.numbers()
            address = person.address()
            numbers_str = ", ".join(numbers) if numbers else "number unknown"
            address_str = address if address else "address unknown"
            return f"{name}: {numbers_str}, {address_str}"
        else:
            return f"{name}: address unknown, number unknown"

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                number = input("number: ")
                self.add_number(name, number)
            elif command == "2":
                name = input("name: ")
                print(self.get_entry(name))  
            elif command == "3":
                name = input("name: ")
                address = input("address: ")
                self.add_address(name, address)
            else:
                print("Invalid command.")


#Usage
#part1
# person = Person("Eric") 
# print(person.name())   
# print(person.numbers())   
# print(person.address())   
# person.add_number("040-123456") 
# person.add_address("Mannerheimintie 10 Helsinki") 
# print(person.numbers())   
# print(person.address())

#part 2
# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# print(phonebook.get_numbers("Eric"))
# print(phonebook.get_numbers("Emily"))

#part 3 
phonebook = PhoneBook()
phonebook.execute()
