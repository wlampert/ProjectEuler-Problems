__author__ = 'WillyLampert'

with open("euler42.txt") as file:
    words = file.readline()
    words = words.replace("\"","")
    words = words.split(",")


letters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F": 6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
triangles = []
word_values = []
count = 0

def triangle(num):
    return (num*(num+1))/2

for i in range(1,100):
    triangles.append(triangle(i))

for word in words:
    temp = 0
    for char in word:
        # For each character, look up its dictionary value, then add that value to a temporary number
        temp += letters[char]
    word_values.append(temp)

for value in word_values:
    if value in triangles:
        count += 1

print count