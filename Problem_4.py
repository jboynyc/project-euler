# http://projecteuler.net/problem=4
def is_palindrome(n):
    if str(n)[0] == str(n)[-1] and str(n)[1] == str(n)[-2] and str(n)[2] == str(n)[-3]:
        return True
    else: 
        return False

l = []
for i in range(100,1000):
    for j in range(100,1000):
        l.append(i*j)

max(filter(is_palindrome, l))