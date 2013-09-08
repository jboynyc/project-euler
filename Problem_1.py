# http://projecteuler.net/problem=1
sum(filter(lambda n: False if n % 3 and n % 5 else True, range(0,1000)))