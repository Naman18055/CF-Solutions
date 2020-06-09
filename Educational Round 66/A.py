t=int(input())
for nt in range(t):
	n,k=map(int,input().split())
	count=0
	while n!=0:
		if n%k==0:
			n=n//k
			count+=1
		else:
			count+=((n%k)+1)
			n=n//k
	print (count-1)