# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.
def countOccurences(n,d):
	count = 0
	while (n):
		if (n%10==d):
			count+=1
		n=int(n/10)
	return count

def mostfrequentdigit(n):
	# your code goes here
	min=0
	result=0
	for i in range(10):
		count1=countOccurences(n,i)
		if (count1<min):
			min = count1
			result=i
	return result
		
