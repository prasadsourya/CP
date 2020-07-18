# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	# Your code goes here
	index=0
	for i in range(len(text)):
		for j in range(i+1):
			if (text[i]==text[j-i]):
				break
		if (j==i):
			text[index]=text[i]
			index+=1
	return ""
