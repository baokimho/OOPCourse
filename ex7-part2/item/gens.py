# Copyright Sami Pyöttiälä 2021






def generate_integers(upper_bound):
   """Creating a generator"""
   for i in range(upper_bound):
       yield i



g = generate_integers(10)
print(type(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())




