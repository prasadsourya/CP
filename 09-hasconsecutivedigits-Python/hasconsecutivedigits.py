# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	if (abs(n)<10):
		return False
	else:
		x=str(abs(n))
		count=0
		for i in range(1,len(x)+1):
			if (x[i-1]==x[i]):
				count+=1
		if count>0:
			return True
		else:
			return False