__author__ = 'WillyLampert'


fib = [0, 1]
seq = []

for i in range(2, 35):
    fib.append((fib[i-1]) + (fib[i-2]))

for i in fib:
    if i < 4000000 and i % 2 == 0:
        seq.append(i)


print fib[1:]
print fib[:1]
print fib[2:5]
print sum(seq)
