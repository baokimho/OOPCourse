class Animal:
    def __init__(self, number_of_legs, age):
        assert isinstance(number_of_legs, int) and number_of_legs > 0, "Number of legs must be a positive integer"
        assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"

        self.__legs = number_of_legs 
        self.__age = age  

    def get_legs(self):
        return self.__legs

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        assert isinstance(new_age, int) and new_age >= 0, "New age must be a non-negative integer"
        self.__age = new_age

    def make_sound(self):
        print("*it's quiet*")

        

