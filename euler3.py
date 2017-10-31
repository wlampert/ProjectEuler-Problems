__author__ = 'WillyLampert'

#Define script functions

def is_prime(num):
    for w in range(2, num/2):
        if num % w == 0:
            return False
    return True


#Start script body
prime_fac = []
fac = []


# for i in range(2, 10000000):
#     if 600851475143 % i == 0:
#         if not is_prime(i):
#             fac.append(i)

x = 600851475143/1471/839


for i in range(2,x):
    if x % i == 0:
        if is_prime(i):
            prime_fac.append(i)



print prime_fac[-1]