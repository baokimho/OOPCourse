from collections import Counter
class ListHelper:
    def __init__(self, my_list):
        self.my_list = my_list
    
    def greatest_frequency(my_list: list):
        most_common = Counter(my_list).most_common(1)[0][0]
        return most_common  

    def doubles(my_list: list):
        counter = Counter(my_list)
        duplicates = [item for item, count in counter.items() if count >= 2]
        return len(duplicates)

numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers)) 
