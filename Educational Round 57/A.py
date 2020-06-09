t=int(input())
x=0
for i in range(t):
	k=list(map(int,input().split()))
	l,m=k[0],k[1]
	for j in range(l,m+1):
		if j*2<=m:
			print (j,j*2)
			break

