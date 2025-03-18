from wolf import Wolf

class Dog(Wolf):
    def __init__(self,breed, age, pack="Domestic"):
        super().__init__(pack, age)
        self.__breed= breed
    
    def make_sound(self):
        print("The dog is barking wooof woof")

    def fetch(self, item):
        print(f"The {self.__breed} dog fetches the {item} happily")

    def wag_tail(self):
        print("The dog wags its tail !")

    def get_breed(self):
        return self.__breed
    
    def set_breed(self, new_breed):
        if new_breed:
            self.__breed = new_breed
        else:
            print("the breed can not be empty")
