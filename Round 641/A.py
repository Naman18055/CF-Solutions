for nt in range(int(input())):
	n,k=map(int,input().split())
	for i in range(2,n+1):
		if n%i==0:
			num=i
			break
	print (n+i+2*(k-1))