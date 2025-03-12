class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight})"
book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
print("Name of the book:", book.name())   
print("Weight of the book:", book.weight())   
print("Book:", book) 
print("Phone:", phone) 