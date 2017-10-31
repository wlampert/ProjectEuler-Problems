__author__ = 'WillyLampert'
import prime

x = 0

for i in range(2,2000000):
    if prime.is_prime(i):
        x += i

print x