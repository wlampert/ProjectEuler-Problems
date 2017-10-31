__author__ = 'WillyLampert'


# 1.23456
larg = []
pal = []
num = []
big_p = []


def is_palindrome(num):
    string_version = str(num)
    string_reversed = string_version[::-1]
    if string_reversed == string_version:
        return True
    return False

def get_palindromes_created_from_three_digit_nums():
    """
    A generator is a function that 'yields' a value. Each time you call it, it will return the 'next' value
    since the last time it's been called.
    """
    for i in range(100, 1000):
        for j in range(100, 1000):
            g = i * j
            if is_palindrome(g):
                yield g

print max(get_palindromes_created_from_three_digit_nums())

# for i in range(100, 1000):
#     for j in range(100, 1000):
#         g = i * j
#         if is_palindrome(g):
#             big_p.append(g)
#
# print max(big_p)



# for i in range(998001):
#     if is_palindrome(i):
#         pal.append(i)
#
# for f in range(100, 1000):
#     for g in pal:
#         if g / f > 99 and g / f < 1000 and g % f == 0:
#             larg.append(g)
#
# len_larg = len(larg)
# print larg[len_larg - 1]

#len_pal = len(pal)
#print pal[len_pal - 1]

#reversed_number = int(string_reversed)