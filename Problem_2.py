# http://projecteuler.net/problem=2
def fibb(max=4000000, l=[1,2]):
    n = l[-1] + l[-2]
    if n < max:
        l.append(n)
        fibb(max,l)
    else:
        return l

sum(filter(lambda x: False if x % 2 else True, fibb()))