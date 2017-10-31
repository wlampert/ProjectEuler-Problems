__author__ = 'WillyLampert'

with open("euler13.txt") as file:
    numbers = file.readlines()

def sum(numbers):
    total = 0
    for token in numbers:
        str(token).replace("\n", "")
    for i in range(100):
       total += int(numbers[i])
    print total




sum(numbers)