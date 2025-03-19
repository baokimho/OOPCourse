from animal import Animal

class Bird(Animal):
    def __init__(self, age):
        assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"
        super().__init__(2, age) 

    def make_sound(self):
        print("*clear bird singing*")
