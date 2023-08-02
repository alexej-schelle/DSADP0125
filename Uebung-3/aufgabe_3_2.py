# Bearbeitet durch Eric Böwer

import math

if __name__ == '__main__':
    # Leibniz formular https://en.wikibooks.org/wiki/Calculus/Leibniz%27_formula_for_pi
    k = 1
    res = 0
    numberOfIteration = 10000000  # Need a lot of iterations to get a precise number
    for i in range(numberOfIteration):
        if i % 2 == 0:
            res += 4 / k
        else:
            res -= 4 / k
        k += 2

    # Cut off after 10 digits
    our_pi = round(res, 10)
    print("Our Approx.:", our_pi)
    print("Goal:", math.pi)
    print("Diff: '{:.10f}'".format(math.pi - our_pi))
