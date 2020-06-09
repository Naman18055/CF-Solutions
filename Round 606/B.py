t=int(input())
for nt in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	d={}
	count=0
	for i in l:
		if i%2==0:
			j=i
			while j not in d and j%2==0:
				d[j]=0
				j=j//2
				count+=1
	print (count)
