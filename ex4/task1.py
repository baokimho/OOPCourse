'''
1️⃣ Encapsulation
✅ Definition:
Encapsulation is an OOP principle that restricts direct access to an 
object’s data and methods.
Instead of accessing data directly, you use getter and setter methods.

✅ Why Use Encapsulation?

Protects data from accidental modification
Hides implementation details from users
Improves code maintainability and security
✅ Example:
'''

class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        """Getter method to access name"""
        return self.__name

    def set_age(self, new_age):
        """Setter method to update age"""
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age!")

# Usage
student = Student("Alice", 20)
print(student.get_name())  # ✅ Correct way to access name
student.set_age(22)        # ✅ Correct way to update age


'''
2️⃣ Client
✅ Definition:
In Object-Oriented Programming (OOP), a client refers to a section of 
code (or another object) that creates an object and uses its methods 
without modifying its internal structure.
✅ Example:
'''
class Calculator:
    def add(self, a, b):
        return a + b

# The client (main function) using Calculator
calc = Calculator()  # ✅ Client creates an object
print(calc.add(5, 3))  # ✅ Client calls a method


'''
3️⃣ Data Attributes
✅ Definition:
Data attributes are variables stored inside an object that hold 
data specific to that instance.

✅ Example:
brand and speed are data attributes because they store specific values 
for each car.
'''
class Car:
    def __init__(self, brand, speed):
        self.brand = brand  # ✅ Data attribute
        self.speed = speed  # ✅ Data attribute

car1 = Car("Toyota", 120)
car2 = Car("BMW", 150)

print(car1.brand)  # ✅ Output: Toyota
print(car2.speed)  # ✅ Output: 150



'''
4️⃣ Instance
✅ Definition:
An instance is an object created from a class.
Each instance has its own set of data attributes and can call the methods 
defined in the class.

✅ Example:
✔ dog and cat are instances of the Animal class.
✔ Each instance has its own data (name is different for each object).
'''
class Animal:
    def __init__(self, name):
        self.name = name

# Creating instances of the Animal class
dog = Animal("Dog")  # ✅ dog is an instance
cat = Animal("Cat")  # ✅ cat is another instance

print(dog.name)  # ✅ Output: Dog
print(cat.name)  # ✅ Output: Cat
