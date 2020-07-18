# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	s_min=min(len(s1),len(s2))
	s_max=max(len(s1),len(s2))
	result=""
	if (s_min==s_max):
		for i in range(s_min):
			result =result +s1[i]+s2[i]
		return result 
	else:
		for i in range(s_min):
			result =result +s1[i]+s2[i]
		for j in range(1,s_max-s_min):
			if(len(s1)>len(s2)):
				result = result+s1[j+1]
			else:
				result=result+s2[j+1]
		return result 

	