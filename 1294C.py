for nt in range(int(input())):
	n = int(input())
	if n<24:
		print ("NO")
		continue
	p = []
	curr = 2
	while curr*curr<n:
		if n%curr==0:
			n=n//curr
			p.append(curr)
		if len(p)==2:
			break
		curr+=1
	if len(p)<=1:
		print ("NO")
		continue
	if n not in p:
		print ("YES")
		print (p[0],p[1],n)
	else:
		print ("NO")