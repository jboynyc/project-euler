# https://projecteuler.net/problem=9
def is_py_trip((a, b, c)):
    return True if (a*a + b*b == c*c) and (a < b < c) else False

import itertools
from operator import mul
r = filter(lambda t: True if sum(t)==1000 and is_py_trip(t) else False, itertools.combinations(xrange(1,998),3))
reduce(mul,r[0])