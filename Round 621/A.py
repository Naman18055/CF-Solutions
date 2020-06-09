for nt in range(int(input())):
	n,d=map(int,input().split())
	l=list(map(int,input().split()))
	ans=0
	for i in range(1,n):
		if l[i]*i<=d:
			ans+=l[i]
			d-=(l[i]*i)
		else:
			ans+=d//i
			break
	print (ans+l[0])