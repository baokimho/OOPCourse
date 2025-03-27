from wolf import Wolf

class Dog(Wolf):
    def __init__(self, breed, age, pack="Domestic"):
        assert isinstance(breed, str) and len(breed) > 0, "Breed must be a non-empty string"
        assert isinstance(pack, str) and len(pack) > 0, "Pack name must be a non-empty string"
        assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"

        super().__init__(pack, age)  
        self.__breed = breed 

    def make_sound(self):
        print("*Dog barking* Woof! Woof!*")

    def fetch(self, item):
        assert isinstance(item, str) and len(item) > 0, "Item must be a non-empty string"
        print(f"*The {self.__breed} dog fetches the {item} happily!*")


    def wag_tail(self):
        print("*The dog wags its tail excitedly!*")

    def get_breed(self):
        return self.__breed

    def set_breed(self, new_breed):
        assert isinstance(new_breed, str) and len(new_breed) > 0, "Breed name must be a non-empty string"
        self.__breed = new_breed
