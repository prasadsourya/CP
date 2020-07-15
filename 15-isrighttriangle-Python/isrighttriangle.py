# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
	b = math.sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2))
	c = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
	x=a*a
	y=b*b
	z=c*c
	if (math.isclose(x+y,z)or(math.isclose(y+z,x))or (math.isclose(x+z,y))):
		return True
	else :
		return False
