import math

__author__ = 'WillyLampert'

PRIME_DIGITS = [2, 3, 5, 7]
truncatable_primes = []
start = input('Start of Range:')
end = input('End of Range:')

prime_number_mappings = [True for x in range(0, end + 1)]
prime_number_mappings[0] = False
prime_number_mappings[1] = False
for i in range(2, int(math.sqrt(end))):
    if prime_number_mappings[i]:
        # If prime_number_mappings's value at [i] is True, the number is prime
        j = i**2
        while j < end:
            prime_number_mappings[j] = False
            j += i


def is_prime(num):
    if prime_number_mappings[num]:
        return True
    return False


def is_truncatable_right(num):
    numstring = str(num)
    ns = numstring[:-1]
    while len(ns) > 1:
        if is_prime(int(ns)):
            ns = ns[:-1]
        else:
            return False
    if len(ns) == 1:
        if int(ns) in PRIME_DIGITS:
            return True
        else:
            return False


def is_truncatable_left(num):
    numstring = str(num)
    ns = numstring[1:]
    while len(ns) > 1:
        if is_prime(int(ns)):
            ns = ns[1:]
        else:
            return False
    if len(ns) == 1:
        if int(ns) in PRIME_DIGITS:
            return True
        else:
            return False


for num in range(start,end):
    if is_prime(num):
        if is_truncatable_right(num):
            if is_truncatable_left(num):
                truncatable_primes.append(num)
                print 'Found prime:', num

print truncatable_primes
print len(truncatable_primes)
print sum(truncatable_primes)

