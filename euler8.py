__author__ = 'WillyLampert'
with open("euler8.txt") as file:
    numbers = file.readlines()
    numbers = numbers[0]

temp = numbers[:13]
x = 1

for y in temp:
    x *= int(y)

for char in numbers[13:]:
    z = 1
    temp2 = temp[1:] + char
    for a in temp2:
        z *= int(a)
    if z > x:
        x = z
    temp = temp2

print x