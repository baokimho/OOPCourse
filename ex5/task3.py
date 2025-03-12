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

# Part 2,3,4

class Suitcase:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.item_store = set()

    def add_item(self, item):
        if item.weight + self.current_weight <= self.max_weight :
            self.current_weight += item.weight
            self.item_store.add(str(item))

    def print_items(self):
        print (", ".join(self.item_store))
    
    def weight(self):
        return self.current_weight
    
    def __str__(self):
        if len(self.item_store) == 1 :
            return f"{len(self.item_store)} item ({self.current_weight} g)"
        else:
            return f"{len(self.item_store)} items ({self.current_weight} g)"
    

# book = Item("ABC Book", 200)   
# phone = Item("Nokia 3210", 100) 
# brick = Item("Brick", 400 ) 
# suitcase = Suitcase(500)   
# print(suitcase) 
# suitcase.add_item(book) 
# print(suitcase) 
# suitcase.add_item(phone)
# print(suitcase) 
# suitcase.add_item(brick)
# print(suitcase)

book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
brick = Item("Brick", 400 ) 
suitcase = Suitcase(1000)   
suitcase.add_item(book) 
suitcase.add_item(phone)
suitcase.add_item(brick)
print("The suitcase contains the following items:") 
suitcase.print_items() 
combined_weight = suitcase.weight() 
print(f"Combined weight: {combined_weight} g") 
