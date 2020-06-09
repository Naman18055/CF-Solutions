from collections import Counter
t=int(input())
for nt in range(t):
	p=input()
	h=input()
	if len(h)<len(p):
		print ("NO")
		continue
	c=Counter(p)
	ans=0
	#print (c)
	for i in range(len(h)-len(p)+1):
		d=Counter(h[i:i+len(p)])
		flag=0
		for j in d:
			if d[j]!=c[j]:
				flag=1
				break
		if flag==0:
			ans=1
			print ("YES")
			break
	if ans==0:
		print ("NO")