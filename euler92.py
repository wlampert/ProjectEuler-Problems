__author__ = 'WillyLampert'

eighty_nines = []
values = [1,89,145,42,20,4,16,37,58]

def number_chain(num):
    x = 0
    while num not in values:
        for char in str(num):
            x += (int(char)) ** 2
        num = x
        x = 0
    if num == 1:
        return False
    return True

for i in range(1,10000000):
    if i % 1000 == 0:
        print i
    if number_chain(i):
        eighty_nines.append(i)

print len(eighty_nines)
