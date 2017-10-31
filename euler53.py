__author__ = 'WillyLampert'
import math

exceeding_vaulues = []

def combinatorics(r, n):
    if (   math.factorial(n)   ) / (   math.factorial(r) * math.factorial(n-r)   ) > 1000000:
        print n, r
        return True
    return False




for n in range(1,101):
    for r in range (2,n+1):
        if combinatorics(r,n):
            exceeding_vaulues.append(n)

print exceeding_vaulues
print len(exceeding_vaulues)
