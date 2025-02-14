class  NumberStats:
    def __init__(self):
        #no need to add any new varibales here, just change the
        #initialization of the self.numbers variable.
        self.numbers = 0
        self.sum = 0 
        self.mean = 0
    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number
    def count_numbers(self):
        return self.numbers
    
    def average(self):
        return self.sum/self.numbers
    def get_sum(self):
        return self.sum
if __name__ == "__main__":
    #Part 1 test prints:
    '''
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers()) '''
    #Part 2 test prints:
    '''
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average()) '''
    #Part 3 test prints:
    '''
    stats = NumberStats()
    list_numbers = []
    print("Please type in interger numbers:")
    a = int(input())
    while a != -1:
        list_numbers.append(int(a))
        a = int(input())
    for i in list_numbers:
        stats.add_number(i)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())  '''
    #Part 4 test prints:
    '''
    stats = NumberStats()
    stats_odd = NumberStats()
    stats_even = NumberStats()
    list_numbers = []
    print("Please type in interger numbers:")
    a = int(input())
    while a != -1:
        list_numbers.append(int(a))
        a = int(input())
    for i in list_numbers:
        stats.add_number(i)
        if i % 2 == 0:
            stats_even.add_number(i)
        else:
            stats_odd.add_number(i)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average()) 
    print("Sum of even numbers:", stats_even.get_sum())
    print("Sum of odd numbers:", stats_odd.get_sum())  '''