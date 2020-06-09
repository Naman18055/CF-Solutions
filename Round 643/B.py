import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	ans=0
	g=1
	m=l[0]
	for i in range(1,n): 
		if g>=m:
			ans+=1
			g=1
			m=l[i]
		else:
			m=max(m,l[i])
			g+=1
		# print (ans,g,m)
	if g>=m:
		ans+=1
	print (ans)