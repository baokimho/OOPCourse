# Running the provided code to ensure there are no errors
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


class Character:
    """
    Represents a player in the game.
    """
    def __init__(self, name, gold):
        """
        Initializes a player with a name, starting gold, and an empty backpack.
        """
        self.__name = name 
        self.__gold = gold
        self.__backpack = []  

    def get_name(self):
        """Returns the name of the player."""
        return self.__name

    def get_gold(self):
        """Returns the amount of gold the player has."""
        return self.__gold

    def get_backpack(self):
        """Returns the player's backpack."""
        return self.__backpack

    def add_gold(self, amount):
        """Adds gold to the player."""
        self.__gold += amount

    def subtract_gold(self, amount):
        """Subtracts gold from the player if they have enough."""
        if self.__gold >= amount:
            self.__gold -= amount
            return True
        return False

    def add_item(self, item):
        """Adds an item to the player's backpack."""
        self.__backpack.append(item)

    def remove_item(self, item):
        """Removes an item from the player's backpack."""
        if item in self.__backpack:
            self.__backpack.remove(item)
            return True
        return False
    
    def show_backpack(self):
        """Returns a list of items in the player's backpack."""
        if not self.__backpack:
            return "The player's backpack is empty."
        return ", ".join(str(item) for item in self.__backpack)

    def __str__(self):
        """Returns a string representation of the player."""
        return f"{self.__name} has {self.__gold} gold and the following items: {self.show_backpack()}"


class NPC(Character):
    """
    Represents the shopkeeper in the game.
    """
    def __init__(self, name= "Shopkeeper"):
        """
        Initializes the shopkeeper with a name and starting gold.
        """
        super().__init__(name, gold=1000)
        self.shop_inventory = []
    
    def add_item_to_shop(self, item):
        """Adds an item to the shop's inventory."""
        self.shop_inventory.append(item)
    
    def show_shop_inventory(self):
        """Returns a list of items in the shop's inventory."""
        if not self.shop_inventory:
            return "The shop's inventory is empty."
        return ", ".join(str(item) for item in self.shop_inventory)


class Shop:
    """
    Represents a shop where the player can buy and sell items.
    """
    def __init__(self, shopkeeper):
        """
        Initializes the shop with a shopkeeper.
        """
        self.shopkeeper = shopkeeper

    def buy_item(self, player, item_name):
        """
        Allows the player to buy an item from the shop.
        """
        for item in self.shopkeeper.shop_inventory:
            if item.get_name() == item_name:
                if player.get_gold() >= item.get_value():
                    player.subtract_gold(item.get_value())
                    player.add_item(item)
                    self.shopkeeper.shop_inventory.remove(item)
                    print(f"{player.get_name()} bought {item.get_name()} for {item.get_value()} gold.")
                    return
                else:
                    print("Not enough gold.")
                    return
        print("Item not found in shop.")

    def sell_item(self, player, item_name):
        """
        Allows the player to sell an item to the shop.
        """
        for item in player.get_backpack():
            if item.get_name() == item_name:
                player.add_gold(item.get_value() // 2)  # Shop buys at half price
                player.remove_item(item)
                self.shopkeeper.shop_inventory.append(item)
                print(f"{player.get_name()} sold {item.get_name()} for {item.get_value() // 2} gold.")
                return
        print("Item not found in backpack.")

    def gamble(self, player, desired_item_name):
        """
        Allows the player to gamble an item for another item in the shop.
        """
        if not player.get_backpack():
            print("Backpack is empty! Cannot gamble.")
            return

        desired_item = None
        for item in self.shopkeeper.shop_inventory:
            if item.get_name() == desired_item_name:
                desired_item = item
                break

        if not desired_item:
            print("The desired item is not in the shop.")
            return

        # Player chooses to gamble
        lost_item = random.choice(player.get_backpack())  # Lose a random item
        player.remove_item(lost_item)

        # 50% chance of success
        if random.random() < 0.5:
            player.add_item(desired_item)
            self.shopkeeper.shop_inventory.remove(desired_item)
            print(f"{player.get_name()} won the gamble and received {desired_item.get_name()}!")
        else:
            print(f"{player.get_name()} lost the gamble and lost {lost_item.get_name()}.")


# Test cases
def test_game():
    # Create the player
    player = Character("Player", 100)

    # Create the shopkeeper
    shopkeeper = NPC("Old Merchant")

    # Create the shop
    shop = Shop(shopkeeper)

    # Add items to the shop
    shopkeeper.add_item_to_shop(Item("Stone Sword", 50))
    shopkeeper.add_item_to_shop(Item("Stone Shield", 30))

    # Player receives some items
    player.add_item(Item("Wooden Stick", 10))
    player.add_item(Item("Old Helmet", 15))

    # Show player and shop inventory
    print(player)
    print("Shop Inventory:", shopkeeper.show_shop_inventory())

    # Player buys an item
    shop.buy_item(player, "Stone Sword")
    print(player)

    # Player sells an item
    shop.sell_item(player, "Old Helmet")
    print(player)

    # Player tries to gamble
    shop.gamble(player, "Stone Shield")
    print(player)

# Run test cases
test_game()
