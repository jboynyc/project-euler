# https://projecteuler.net/problem=7

is_prime = lambda n: not len(filter(lambda x: not n % x, range(2,int(round(sqrt(n)))+1)))

def nth_prime(n, c=1, p=2):
    if c==n: 
        return p
    else:
        if is_prime(p+1): return nth_prime(n, c+1, p+1)
        else: return nth_prime(n, c, p+1)
    
nth_prime(10001) # exceeds maximum recursion depth; use nth-prime.scm instead
