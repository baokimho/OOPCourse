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

# Part 2,3,4,5

class Suitcase:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.items = []  

    def add_item(self, item):
        current_weight = self.weight()
        if item.weight + current_weight <= self.max_weight:
            self.items.append(item)  

    def print_items(self):
        item_strings = [str(item) for item in self.items]
        print(", ".join(item_strings))
    
    def weight(self):
        return sum(item.weight for item in self.items)

    def heaviest_item(self):
        if not self.items:
            return None
        return max(self.items, key=lambda item: item.weight)  
    
    def __str__(self):
        if len(self.items) == 1 :
            return f"{len(self.items)} item ({self.weight()} g)"
        else:
            return f"{len(self.items)} items ({self.weight()} g)"

class CargoHold:
    def __init__(self, maximum_weight):
        self.maximum_weight = maximum_weight* 1000
        self.items = []  
    
    def add_suitcase(self, suitcase):
        if suitcase.weight() + self.weight() <= self.maximum_weight:
            self.items.append(suitcase)
    
    def weight(self):
        return sum(item.weight() for item in self.items) 
       
    def print_items(self):
        for suitcase in self.items:
            for item in suitcase.items:
                print(item)
    
    def __str__(self):
        remaining_space = self.maximum_weight - self.weight()
        if len(self.items) == 1:
            return f"{len(self.items)} suitcase, space for {remaining_space/1000} kg"
        else:
            return f"{len(self.items)} suitcases, space for {remaining_space/1000} kg"

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

# book = Item("ABC Book", 200)   
# phone = Item("Nokia 3210", 100) 
# brick = Item("Brick", 400 ) 
# suitcase = Suitcase(1000)   
# suitcase.add_item(book) 
# suitcase.add_item(phone)
# suitcase.add_item(brick)
# print("The suitcase contains the following items:") 
# suitcase.print_items() 
# combined_weight = suitcase.weight() 
# print(f"Combined weight: {combined_weight} g") 

# book = Item("ABC Book", 200)   
# phone = Item("Nokia 3210", 100) 
# brick = Item("Brick", 400 ) 
# suitcase = Suitcase(1000)   
# suitcase.add_item(book) 
# suitcase.add_item(phone)
# suitcase.add_item(brick)
# heaviest = suitcase.heaviest_item() 
# print(f"The heaviest item: {heaviest}") 

# cargo_hold = CargoHold(100) 
# print(cargo_hold)
# book = Item("ABC Book", 200)   
# phone = Item("Nokia 3210", 100) 
# brick = Item("Brick", 400 ) 
# adas_suitcase = Suitcase(1000) 
# adas_suitcase.add_item(book) 
# adas_suitcase.add_item(phone)
# peters_suitcase = Suitcase(1000)
# peters_suitcase.add_item(brick)
# cargo_hold.add_suitcase(adas_suitcase) 
# print(cargo_hold) 
# cargo_hold.add_suitcase(peters_suitcase)
# print(cargo_hold)

book = Item("ABC Book", 200)   
phone = Item("Nokia 3210", 100) 
brick = Item("Brick", 400 ) 
adas_suitcase = Suitcase(1000) 
adas_suitcase.add_item(book) 
adas_suitcase.add_item(phone)
peters_suitcase = Suitcase(1000)
peters_suitcase.add_item(brick)
cargo_hold = CargoHold(100) 
cargo_hold.add_suitcase(adas_suitcase) 
cargo_hold.add_suitcase(peters_suitcase)
print("The suitcases in the cargo hold contain the following items:") 
cargo_hold.print_items()

