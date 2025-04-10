# Copyright Sami Pyöttiälä 2021



from functools import reduce


add_ten = lambda x: x + 10

print(add_ten(5)) 
print(add_ten(101))
print(add_ten(add_ten(add_ten(add_ten(add_ten(0))))))




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(even_numbers)
print(odd_numbers)



numbers = [1, 2, 3, 4, 5, 66, 7, 8, 9, 10]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)


numbers = [2, 3, 5, ]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)



