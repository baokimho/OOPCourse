import random

# Initialize empty lists
number_list = []
string_list = []

# Fill the number list with user input
print("Enter 10 numbers:")
for _ in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)

# Fill the string list with user input
print("Enter 10 strings:")
for _ in range(10):
    string = input("Enter a string: ")
    string_list.append(string)

# Print both lists
print("Number List:", number_list)
print("String List:", string_list)

# Fill the number list with randomly generated numbers
number_list = [random.randint(1, 100) for _ in range(10)]

# Print the new number list
print("Random Number List:", number_list)
