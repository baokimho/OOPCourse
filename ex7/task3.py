

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
        else:
            self.__address = address

    def add_number(self, number):
        if number in self.__numbers:
            return  
        else:
            self.__numbers.append(number)  


#Usage
person = Person("Eric") 
print(person.name())   
print(person.numbers())   
print(person.address())   
person.add_number("040-123456") 
person.add_address("Mannerheimintie 10 Helsinki") 
print(person.numbers())   
print(person.address())