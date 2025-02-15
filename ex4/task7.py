class Person:
    def __init__(self, name:str, height: int):
        self.name = name
        self.height = height   

    def __str__(self):
        return self.name + " is " + str(self.height) + " cm tall."
class Room:
    def __init__(self):
        self.people = []
    
    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0 
    
    def total_height(self):
        return sum([person.height for person in self.people])
        
    def print_contents(self):
        print("There are", len(self.people), "people in the room, and their combined height is:", self.total_height(), "cm")
        for person in self.people:
            print(person)


#Example of Usage
room = Room() 
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183)) 
room.add(Person("Kenya", 172)) 
room.add(Person("Ally", 166)) 
room.add(Person("Nina", 162)) 
room.add(Person("Dorothy", 175)) 
print("Is the room empty?", room.is_empty())
room.print_contents()
