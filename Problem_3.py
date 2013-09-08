# http://projecteuler.net/problem=3
def factors_of(n):
    return filter(lambda x: not n % x, range(1,int(n**.5)))

is_prime = lambda n: not len(filter(lambda x: not n % x, range(2,int(round(sqrt(n)))+1)))

max(filter(is_prime, factors_of(600851475143))) 