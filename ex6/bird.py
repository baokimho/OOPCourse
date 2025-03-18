from animal import Animal

class Bird(Animal):

    def __init__(self, age):
        super().__init__(2,age)

    def make_sound(self):
        print("*clear bird singing*")
        