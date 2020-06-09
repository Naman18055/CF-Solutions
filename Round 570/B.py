t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	total=[max(l[0]-k,1),l[0]+k]
	for i in l:
		if max(i-k,1)>total[0]:
			total[0]=max(i-k,1)
		if (i+k)<total[1]:
			total[1]=(i+k)
	if total[0]>total[1]:
		print (-1)
	else:
		print (total[1])
