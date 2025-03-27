import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.side = None

    def roll(self):
        self.side = random.randint(1, self.sides)
        return self.side

    def get_side(self):
        return self.side

    def __str__(self):
        return f"Dice shows {self.side}" if self.side else "Dice not rolled yet"

class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()
        self._pet = None

    @property
    def pet(self):
        return self._pet

    @pet.setter
    def pet(self, mammal):
        self._pet = mammal

    def roll_dice(self):
        return self.dice.roll()

    def __str__(self):
        pet_info = f"Pet: {self.pet}" if self.pet else "No pet yet"
        return f"Player {self.name} (ID: {self.player_id}) - {pet_info}"

class Mammal:
    def __init__(self, id, species, name, size, weight):
        self.id = id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight

    def __str__(self):
        return f"Mammal ID: {self.id}, Species: {self.species}, Name: {self.name}, Size: {self.size}, Weight: {self.weight}kg"

mammals_list = [
    Mammal(1, "Mouse", "Jerry", "Small", 0.1),
    Mammal(2, "Cat", "Whiskers", "Medium", 4),
    Mammal(3, "Dog", "Buddy", "Medium", 10),
    Mammal(4, "Wolf", "Fang", "Large", 40),
    Mammal(5, "Lion", "Simba", "Large", 150),
    Mammal(6, "Elephant", "Dumbo", "Huge", 5000)
]

def roll_dice_game(num_dices):
    dices = [Dice() for _ in range(num_dices)]
    total = sum(d.roll() for d in dices)
    print(f"Rolled {num_dices} dice(s): {total}")
    return total


#usage
num_players = int(input("Enter number of players: "))
players = {}
    
for i in range(1, num_players + 1):
    name = input(f"Enter name for player {i}: ")
    players[i] = Player(name, i)
    
    # Rolling dice for each player
for player in players.values():
    print(f"{player.name} is rolling their dice...")
    player.roll_dice()
    print(f"{player.name} rolled: {player.dice.get_side()}")
    
    # Assign pets based on dice sum
for player in players.values():
    dice_sum = roll_dice_game(2)
    pet_index = min(dice_sum // 2, len(mammals_list) - 1)  # Prevent index out of range
    player.pet = mammals_list[pet_index]
    print(f"{player.name} got pet: {player.pet}")
   
print("\nFinal Player and Pet Summary:")
for player in players.values():
    print(player)
