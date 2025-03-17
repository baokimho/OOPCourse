class Animal:

    def __init__(self, number_of_legs, age):
        self.legs = number_of_legs
        self.age = age

    def number_of_legs(self): 
        return self.legs

    def make_sound(self):
        print("*it's quiet*")
    
    def get_age(self):
        return self.age
        
        