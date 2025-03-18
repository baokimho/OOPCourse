# class Animal:

#     def __init__(self, number_of_legs, age):
#         self.legs = number_of_legs
#         self.age = age

#     def number_of_legs(self): 
#         return self.legs

#     def make_sound(self):
#         print("*it's quiet*")
    
#     def get_age(self):
#         return self.age
        
        
class Animal:
    def __init__(self, number_of_legs, age):
        self.__legs = number_of_legs  
        self.__age = age  

    def get_legs(self): 
        return self.__legs

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Age cannot be negative!")

    def make_sound(self):
        print("*it's quiet*")
