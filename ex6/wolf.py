from mammal import Mammal

class Wolf(Mammal):
    def __init__(self, pack, age):
        super().__init__(age)
        self.__pack_name = pack  

    def get_pack_name(self):
        return self.__pack_name

    def set_pack_name(self, new_pack):
        if new_pack:
            self.__pack_name = new_pack
        else:
            print("Pack name cannot be empty!")

    def another_make_sound(self):
        print("*wolf howling*")