# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def is_prime_number(n):
	count=0
	for i in range(1,n+1):
		if (n%i==0):
			count=count+1
	if (count==2):
		return True
	else:
		return False

def is_happy_number(n):
	past=set()
	while(n!=1):
		n=sum(int(i)**2 for i in str(n))
		if n in past:
			return False
		past.add(n)
	return True

def fun_nth_happy_prime(n):
	happy_prime_numbers=[x for x in range(500) if (is_happy_number(x) and is_prime_number(x))][:n]
	return happy_prime_numbers[n-1]