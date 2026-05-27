"""
a program that creates a list of 20 random numbers in the range from 1 to 100 using List Comprehension.

Then, using List Comprehension, create a new list containing only the even numbers from the original list.

The program should output both lists.

"""

import random

random_numbers=[random.randint(1,100) for _ in range(20)]

even_number=[num for num in  random_numbers if num%2==0]

print("Orginal random number list",random_numbers)

print("Even list ",even_number)

