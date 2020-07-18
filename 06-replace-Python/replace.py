# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	temp=""
	for i in range(len(s1)):
		for j in range(i,len(s2)+i):
			temp=temp+s1[j]
			if (temp==s2):
				temp==s3
		temp=temp+s1[i]		
	return temp

