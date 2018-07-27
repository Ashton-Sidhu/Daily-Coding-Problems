#QUESTION
#The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#Hint: The basic equation of a circle is x2 + y2 = r2.

#SOLUTION
#Estimate Area using area of a square using the points x and y, therefore the equation is A(square) = (2r)^2 and pi can be estimated using the following method:
# - Divide the area of of a circle by the area of the square = pi/4
# - Generate a set of points x and y. If the point lands within the circle add that to a counter.
# - Estimate pi using ratio of the number of random numbers that land inside in the circle by the total * 4

import math
import random

def EstimatePi(x, y):

    r_sq = x ** 2 + y ** 2
    r = math.sqrt(r_sq)
    numerator = (2*r) ** 2

    return numerator / r_sq

def main():
    N = 1000000
    inside = 0
    for _ in range(N):

        x = random.random() ** 2
        y = random.random() ** 2

        if math.sqrt(x+y) < 1:
            inside += 1

    print(round(float(inside/N) * 4, 3))

if __name__ == '__main__':
    main()