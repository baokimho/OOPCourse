# Part 1
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight})"
book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
# print("Name of the book:", book.name())   
# print("Weight of the book:", book.weight())   
# print("Book:", book) 
# print("Phone:", phone) 

# Part 2

class Suitcase:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.item_store = set()
    def add_item(self, item):
        if item.weight + self.current_weight <= self.max_weight :
            self.current_weight += item.weight
            self.item_store.add(item)
    
    def __str__(self):
        return f"{len(self.item_store)} item ({self.current_weight} g)"

book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
brick = Item("Brick", 400 ) 
suitcase = Suitcase(500)   
print(suitcase) 
suitcase.add_item(book) 
print(suitcase) 
suitcase.add_item(phone)
print(suitcase) 
suitcase.add_item(brick)
print(suitcase)