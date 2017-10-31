__author__ = 'WillyLampert'

primes = [2,3,5]


def is_prime(num):
    for i in range(2,num/2):
        if num % i ==0:
            return False
    return True

for n in range(2,110000):
    if n % 2 != 0 and n % 3 != 0 and n % 4 != 0 and n % 5 != 0:
        if is_prime(n):
            primes.append(n)

print primes[10000]
print len(primes)

#5133
#1802
#1788
#879
#861