from mammal import Mammal

class Wolf(Mammal):

    def __init__(self, pack, age):
        super.__init__(age)
        self.pack_name = pack

    def another_make_sound(self):
        print("*wolf howling*")
        