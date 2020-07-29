# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
l=[]
import math
def prime_factors(n):
    while(n%2==0):
        l.append(2)
        n=n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            l.append(i)
            n=n//i
    if n>2:
        l.append(n)
        return l

def is_smith(n):
    a=sum(list(map(int,str(n))))

def fun_nth_smithnumber(n):
    return 1