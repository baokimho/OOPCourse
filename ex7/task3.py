

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
            return  False
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
            return None
        return self.__persons[name].numbers()

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
phonebook = PhoneBook()
phonebook.add_number("Eric", "02-123456")
print(phonebook.get_numbers("Eric"))
print(phonebook.get_numbers("Emily"))