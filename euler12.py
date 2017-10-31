__author__ = 'WillyLampert'
import math
end = 1000000
triangles = [1,3,6,10,15,21,28]

def triangle_numbers(num):
    t = num * ((.5 * num) + .5)
    triangles.append(int(t))
    return int(t)

prime_number_mappings = [True for l in range(0, end + 10)]
prime_number_mappings[0] = False
prime_number_mappings[1] = False
for i in range(2, int(math.sqrt(end+10))):
    if prime_number_mappings[i]:
        j = i**2
        while j < end:
            prime_number_mappings[j] = False
            j += i

def factors(num):
    temp = []
    temp2 = []
    t = 1
    for idx, x in enumerate(prime_number_mappings):
        if num == 1:
            break
        if x and num % (idx) == 0:
            while num != 1 and num % (idx) == 0:
                num /= (idx)
                temp.append(idx)
    for y in temp:
        temp2.append(temp.count(y))
        temp = [h for h in temp if h != y]
        temp2 = [z for z in temp2 if z != 0]
    for idx,z in enumerate(temp2):
        temp2[idx] += 1
    for a in temp2:
        t *= a
    if t > 500:
        return True
    return False

# def factors(num):
#     facs = [1]
#     for w in range(2,int(num/2)):
#         if num % w == 0:
#             facs.append(w)
#             if len(facs) > 250:
#                 return True
#     return False


for i in (range(8,100000)):
    if i % 1000 == 0:
        print i
    if factors(triangle_numbers(i)):
        print triangle_numbers(i)

