t=int(input())
for nt in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	m=l[-1]
	count=0
	for i in range(n-2,-1,-1):
		if l[i]>m:
			count+=1
		else:
			m=l[i]
	print (count)
