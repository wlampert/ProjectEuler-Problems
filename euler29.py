__author__ = 'WillyLampert'


ints = []

for a in range(2,101):
    for b in range(2,101):
        n = a**b
        if n not in ints:
            ints.append(n)

print len(ints)