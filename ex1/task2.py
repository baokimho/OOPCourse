import random

number_list = []
string_list = []

print("Enter 10 numbers:")
for _ in range(10):
    number = int(input("Enter a number: "))
    number_list.append(number)

print("Enter 10 strings:")
for _ in range(10):
    string = input("Enter a string: ")
    string_list.append(string)

print("Number List:", number_list)
print("String List:", string_list)

number_list = [random.randint(1, 100) for _ in range(10)]

print("Random Number List:", number_list)
