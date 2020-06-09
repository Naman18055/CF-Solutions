for nt in range(int(input())):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	a.sort()
	b.sort(reverse=True)
	s=0
	for i in range(k):
		if b[i]>=a[i]:
			s+=(b[i]-a[i])
		else:
			break
	print (sum(a)+s)