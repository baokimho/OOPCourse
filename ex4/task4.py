class LunchCard:
    def __init__(self, owner: str, balance: float):

        self.owner = owner
        self.balance = balance

    def deposit_money(self, amount: float):

        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Invalid amount. Deposit must be positive.")

    def eat_ordinary(self):

        if self.balance >= 2.95:
            self.balance -= 2.95
        else:
            print(f"Not enough balance on {self.owner}'s card.")    

    def eat_luxury(self):

        if self.balance >= 5.90:
            self.balance -= 5.90
        else:
            print(f"Not enough balance on {self.owner}'s card.")

    def __str__(self):

        return f"{self.owner}: The balance is {round(self.balance,2)} euros"

def main():
    # Step 1: Create LunchCards for Peter and Grace
    peter_card = LunchCard("Peter", 20)
    grace_card = LunchCard("Grace", 30)

    # Step 2: Perform lunch transactions
    peter_card.eat_luxury()    # Peter eats a luxury lunch
    grace_card.eat_ordinary()  # Grace eats an ordinary lunch

    # Step 3: Print balances
    print(peter_card)
    print(grace_card)

    # Step 4: Peter deposits 20 euros
    peter_card.deposit_money(20)

    # Step 5: Grace eats a special meal (luxury)
    grace_card.eat_luxury()

    # Step 6: Print updated balances
    print(peter_card)
    print(grace_card)

    # Step 7: More transactions
    peter_card.eat_ordinary()
    peter_card.eat_ordinary()
    grace_card.deposit_money(50)

    # Step 8: Print final balances
    print(peter_card)
    print(grace_card)



if __name__ == "__main__":
    #Part1
    '''
    card = LunchCard(50)
    print(card)
    '''
    #Part2
    '''
    card = LunchCard(11)
    print(card)

    card.eat_ordinary()
    print(card)

    card.eat_luxury()
    card.eat_ordinary()
    print(card)
    '''
    #Part3
    '''
    card = LunchCard(10) 
    print(card) 
    card.deposit_money(15) 
    print(card) 
    card.deposit_money(10 ) 
    print(card) 
    card.deposit_money(200) 
    #card.deposit_money(-100)
    print(card)
    '''
    #Part4
    main()