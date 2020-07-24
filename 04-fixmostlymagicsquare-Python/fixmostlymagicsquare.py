# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# Your code goes here
	l=[]
	l1=[]
	a,s1=0,0
	rowid,colid=0,0
	for i in L:
		l.append(sum(i))
	for j in L:
		if(l.count(j)==1):
			rowid=l.index(j)
	for x in range(len(L)):
		for y in L:
			s=s+y[x]
		l1.append(s)
		s=0
	for z in l1:
		if l1.count(z)==1:
			s=z
			colid=l1.index(z)
	s0=l1[colid-1]
	l[rowlid][colid]=((L[rowlid][colid]))