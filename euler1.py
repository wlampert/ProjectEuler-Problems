__author__ = 'WillyLampert'

three_multiples = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        three_multiples.append(i)

print three_multiples
print sum(three_multiples)
print "Test"

print 'Kyles version', sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
