from mammal import Mammal

class Wolf(Mammal):
    def __init__(self, pack, age):
        assert isinstance(pack, str) and len(pack) > 0, "Pack name must be a non-empty string"
        assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"

        super().__init__(age)  
        self.__pack_name = pack  

    def get_pack_name(self):
        return self.__pack_name

    def set_pack_name(self, new_pack):
        assert isinstance(new_pack, str) and len(new_pack) > 0, "New pack name must be a non-empty string"
        self.__pack_name = new_pack

    def make_sound(self):
        print("*Wolf howling*")
