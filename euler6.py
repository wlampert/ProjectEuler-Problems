__author__ = 'WillyLampert'

sqrs = []
sums = []

for i in range(1,101):
    sqrs.append(i ** 2)

sqrs_final = sum(sqrs)

for j in range(1,101):
    sums.append(j)

sums_final = sum(sums) ** 2

dif_of_sqrs = sums_final - sqrs_final

print dif_of_sqrs