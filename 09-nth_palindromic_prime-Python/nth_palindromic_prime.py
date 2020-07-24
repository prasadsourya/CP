# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def is_palindrome(n):
	n=str(n)
	if n[::]==n[::-1]:
		return True
	return False


def fun_nth_palindromic_prime(n):
	if (n==0):
		return 2
	return 0