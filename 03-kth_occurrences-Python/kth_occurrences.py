# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dic={}
	s=s.replace(" ","")
	for i in s:
		if i not in dic:
			dic[i]=s.count(i)
	sort_dic=sorted(dic.items(),key=lambda x:x[1], reverse =True)
	if (len(sort_dic)<n):
		a=sort_dic[0]
		
	return 'a'


