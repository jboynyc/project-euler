#https://projecteuler.net/problem=10
is_prime = lambda n: not len(filter(lambda x: not n % x, range(2,int(round(sqrt(n)))+1)))

sum(filter(is_prime, xrange(2,2000000))) # slow; use sum-of-primes.scm instead
