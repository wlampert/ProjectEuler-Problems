__author__ = 'WillyLampert'


trips = []
sums = []

def pyth_trip(num):
    for a in range(1,num):
        for b in range(1,num):
            for c in range(1,num):
                if a < b and b < c and a**2 + b**2 == c**2 and a + b + c == 1000:
                    print a, b, c, a * b * c


pyth_trip(500)
