import random

class Item:
    """
    Represents an item in the game.
    """
    def __init__(self, name, value):
        """
        Initializes an item with a name and value.
        """
        self.__name = name
        self.__value = value 

    def get_name(self):
        """Returns the name of the item."""
        return self.__name

    def get_value(self):
        """Returns the value of the item."""
        return self.__value

    def __str__(self):
        """Returns a string representation of the item."""
        return f"{self.__name} costs {self.__value} gold."


class Player:
    """
    Represents a player in the world.
    """
    def __init__(self, name, gold=100, x=0, y=0):
        """
        Initializes a player with a name, gold, position, and an empty backpack.
        """
        self.__name = name
        self.__gold = gold
        self.__x = x  # X position in the grid
        self.__y = y  # Y position in the grid
        self.__backpack = []

    def get_name(self):
        """Returns the name of the player."""
        return self.__name

    def get_position(self):
        """Returns the current position of the player (x, y)."""
        return (self.__x, self.__y)

    def move(self, direction, world):
        """
        Moves the player in a specified direction within the world.

        :param direction: 'N', 'S', 'E', 'W' (North, South, East, West)
        :param world: The world object to check for valid moves.
        """
        new_x, new_y = self.__x, self.__y

        if direction == "N":
            new_y -= 1
        elif direction == "S":
            new_y += 1
        elif direction == "E":
            new_x += 1
        elif direction == "W":
            new_x -= 1
        else:
            print("Invalid direction! Use 'N', 'S', 'E', 'W'.")
            return

        if world.is_valid_position(new_x, new_y):
            world.move_player(self, new_x, new_y)
            self.__x, self.__y = new_x, new_y
            print(f"{self.__name} moved to ({self.__x}, {self.__y}).")
        else:
            print("Cannot move outside the world boundaries!")

    def pick_up_item(self, world):
        """
        Picks up an item from the current grid cell in the world.
        """
        item = world.pickup_item(self)
        if item:
            self.__backpack.append(item)
            print(f"{self.__name} picked up {item.get_name()}!")

    def show_backpack(self):
        """Returns a list of items in the player's backpack."""
        if not self.__backpack:
            return "The backpack is empty."
        return ", ".join(str(item) for item in self.__backpack)

    def __str__(self):
        """Returns a string representation of the player."""
        return f"{self.__name} at ({self.__x}, {self.__y}) with {self.__gold} gold. Items: {self.show_backpack()}"


class GridCell:
    """
    Represents a single cell in the grid-based world.
    """
    def __init__(self):
        """
        Initializes an empty cell with no player and no item.
        """
        self.__player = None
        self.__item = None

    def place_player(self, player):
        """Places a player in the cell."""
        self.__player = player

    def remove_player(self):
        """Removes the player from the cell."""
        self.__player = None

    def place_item(self, item):
        """Places an item in the cell."""
        self.__item = item

    def remove_item(self):
        """Removes the item from the cell and returns it."""
        item = self.__item
        self.__item = None
        return item

    def get_item(self):
        """Returns the item in the cell."""
        return self.__item

    def __str__(self):
        """Returns a string representation of the cell."""
        if self.__player:
            return f"[P:{self.__player.get_name()}]"
        elif self.__item:
            return f"[I:{self.__item.get_name()}]"
        else:
            return "[ ]"


class World:
    """
    Represents the grid-based world where players and items exist.
    """
    def __init__(self, width, height):
        """
        Initializes the world with a grid of given width and height.
        """
        self.__width = width
        self.__height = height
        self.__grid = [[GridCell() for _ in range(width)] for _ in range(height)]
        self.__players = []
        self.__items = []

    def is_valid_position(self, x, y):
        """Checks if the position is within world boundaries."""
        return 0 <= x < self.__width and 0 <= y < self.__height

    def add_player(self, player, x, y):
        """
        Adds a player to the world at a given position.
        """
        if self.is_valid_position(x, y):
            self.__players.append(player)
            self.__grid[y][x].place_player(player)
            print(f"Added player {player.get_name()} at ({x}, {y}).")
        else:
            print("Invalid player position!")

    def add_item(self, item, x, y):
        """
        Adds an item to the world at a given position.
        """
        if self.is_valid_position(x, y):
            self.__items.append(item)
            self.__grid[y][x].place_item(item)
            print(f"Placed {item.get_name()} at ({x}, {y}).")
        else:
            print("Invalid item position!")

    def move_player(self, player, new_x, new_y):
        """
        Moves the player from their current position to a new position.
        """
        old_x, old_y = player.get_position()
        self.__grid[old_y][old_x].remove_player()
        self.__grid[new_y][new_x].place_player(player)

    def pickup_item(self, player):
        """
        Allows a player to pick up an item from their current position.
        """
        x, y = player.get_position()
        item = self.__grid[y][x].remove_item()
        if item:
            self.__items.remove(item)
            return item
        print("No item to pick up here.")
        return None

    def show_grid(self):
        """
        Displays the world grid with players and items.
        """
        for row in self.__grid:
            print(" ".join(str(cell) for cell in row))
        print()

""" TEST CASES """
if __name__ == "__main__":
    #Create a world
    world = World(5, 5)

    # Create players
    player1 = Player("Alice", x=1, y=1)
    player2 = Player("Bob", x=3, y=3)

    # Create items
    sword = Item("Stone Sword", 50)
    shield = Item("Stone Shield", 30)

    # Add players and items to the world
    world.add_player(player1, 1, 1)
    world.add_player(player2, 3, 3)
    world.add_item(sword, 2, 2)
    world.add_item(shield, 4, 4)

    # Display the world grid
    world.show_grid()

    # Move players and pick up items
    player1.move("E", world)  # Move East
    player1.pick_up_item(world)  # Pick up the sword
    player2.move("W", world)  # Move West

    # Display updated world grid
    world.show_grid()

    # Show players' status
    print(player1)
    print(player2)
