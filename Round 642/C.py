for nt in range(int(input())):
	n=int(input())
	if n==1:
		print (0)
		continue
	ans=0
	k=3
	for i in range(1,n//2+1):
		ans+=(i*(4*k-4))
		k+=2
	print (ans)