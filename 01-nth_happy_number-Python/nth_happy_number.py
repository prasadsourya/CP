# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)
def is_happy_number(n):
	past =set()
	while n!=1:
		n=sum(int(i)**2 for i in str(n))
		if n in past:
			return False
		past.add(n)
	return True

def fun_nth_happy_number(n):

	happy_numbers=[i for i in range(500) if is_happy_number(i)][:n+1]
	return happy_numbers[-1]

