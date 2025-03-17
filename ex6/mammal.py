from animal import Animal

class Mammal(Animal):

    def __init__(self, age):
        super.__init__(4, age)

    def make_sound(self): 
        print("*mammal breathing*")
        