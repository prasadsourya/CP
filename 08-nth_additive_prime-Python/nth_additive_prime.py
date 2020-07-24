# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
def is_prime(n):
	if n<=1:
		return False
	for i in range(2,m):
		if (n%i==0):
			return False
	return True



def fun_nth_additive_prime(n):
	return 1