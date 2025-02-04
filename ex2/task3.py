# File:          coin.py
# Source:        Tony Gaddis: Starting Out with Python, fourth edition
# Modified by:   Sanna Maatta & Anne Jumppanen
# Description:   Coin object and tossing

import random

# Class definition
class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.choices([
            'Heads', 'Tails', 'Upright on the table',
            'Disappeared in a rabbit hole', 'Lost in a wormhole in space'
        ], weights=[0.45, 0.45, 0.07, 0.025, 0.005], k=1)[0]
        
        self.sideup = outcome
        
        if outcome == 'Heads' or outcome == 'Tails':
            print(f"The coin lands showing {outcome}!")
        elif outcome == 'Upright on the table':
            print("The coin miraculously lands upright on its edge!")
        elif outcome == 'Disappeared in a rabbit hole':
            print("Oh no! The coin drops to the ground and disappears into a rabbit hole!")
        elif outcome == 'Lost in a wormhole in space':
            print("Unbelievable! The coin defies gravity and vanishes into a wormhole in space!")

    def get_sideup(self):
        return self.sideup

# Main function definition
def main():
    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

# Calling the main function
main()
