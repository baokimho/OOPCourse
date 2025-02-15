class BankAccount:
    #constructor
    def __init__(self,owner: str, account_number: str, balance: float):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Deposit amount must be positive.")
        
    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("Withdrawal amount must be positive and not exceed the balance.")
    @property
    def balance(self):
        return round(self.__balance, 2)
    
    def __service_charge(self):
        self.__balance -= self.__balance * 0.01
    
    def __str__(self):  
        return f"{self.__owner}, {self.__account_number}, balance: {self.__balance}"
    

account = BankAccount("Randy Riches", "12345-6789", 1000) 
account.withdraw(100) 
print(account.balance) 
account.deposit(100) 
print(account.balance)

