for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	flag=0
	d={}
	for i in range(n):
		if l[i] not in d:
			d[l[i]]=[i]
		else:
			d[l[i]].append(i)
	for i in d:
		if len(d[i])>2:
			print ("YES")
			flag=1
			break
		elif len(d[i])==2:
			if d[i][1]-d[i][0]>1:
				print ("YES")
				flag=1
				break
	if flag==0:
		print ("NO")