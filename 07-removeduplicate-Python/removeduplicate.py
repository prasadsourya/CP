# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	text1=list(text)
	index=0
	for i in range(0,len(text1)):
		for j in range(0,i+1):
			if (text1[i]==text1[j]):
				break
		if (j==i):
			text1[index]=text1[i]
			index+=1
	return "".join(text1[:index])
