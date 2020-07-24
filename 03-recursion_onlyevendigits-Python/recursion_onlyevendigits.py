# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
def get_even_digit(x,i):
	if i==len(x):
		if i==0:
			return 0
		return int(x)
	y=x[i]
	if y%2==0:
		return get_even_digit(x,i+1)
	else:
		return get_even_digit(x[:i]+x[i+1],i)

def fun_recursion_onlyevendigits(l): 
		if l==[]:return []
		for i in range(len(l)):
			l[i]=get_even_digit()