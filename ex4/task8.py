class Recording:
    def __init__(self, length: int):
        self.__length = length  # Private attribute

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length: int):
        if isinstance(new_length, int) and new_length > 0:
            self.__length = new_length
        else:
            raise ValueError("Length must be a positive integer.")

the_wall = Recording(43)
print(the_wall.length)  

the_wall.length = 44
print(the_wall.length) 
