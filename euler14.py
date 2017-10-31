__author__ = 'WillyLampert'


def collatz(num):
    longest = 0
    length = 0
    for i in reversed(range(10, num)):
        original = i
        temp = [i]
        while i != 1:
            if i % 2 == 0:
                i = i / 2
                temp.append(i)
            else:
                i = (i * 3) + 1
                temp.append(i)
        if len(temp) > length:
            longest = original
            length = len(temp)
            print longest
    return longest


print collatz(1000000)

