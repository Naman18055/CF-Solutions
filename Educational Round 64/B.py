import sys
t=int(input())
for naman in range(t):
	s=input()
	d={}
	for i in s:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	s1=[]
	for i in d:
		s1.append(ord(i))
	s1=sorted(s1)
	if len(s1)>3:

	else:
		print ("No answer")
		sys.exit()
