"""
Write a program that creates a list of 10 integers.


Using a for loop, replace all even elements of the list with the string "even".

The program should output the updated list.
"""

numbers=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(numbers)):
    if numbers[i]%2==0:
        numbers[i]="Even"
print(numbers)