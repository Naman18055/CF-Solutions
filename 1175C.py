import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort()
	m=10**9	
	ans=-1
	for i in range(k,n):
		dist = l[i]-l[i-k]
		if dist<m:
			m=dist
			ans=l[i-k]+dist//2
	print (ans)