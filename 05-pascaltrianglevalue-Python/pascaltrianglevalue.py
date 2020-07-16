# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 
from math import factorial

def combination(n,k):
	return int(factorial(n)/(factorial(k)*factorial(n-k)))


def fun_pascaltrianglevalue(row, col):
	result = combination(row,col)
	return result