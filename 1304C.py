import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,m=map(int,input().split())
	cus = []
	for i in range(n):
		cus.append(list(map(int,input().split())))
	l,e=m,m
	p=0
	ans="YES"
	for i in range(n):
		l-=(cus[i][0]-p)
		e+=(cus[i][0]-p)
		l=(max(l,cus[i][1]))
		e=(min(e,cus[i][2]))
		p=cus[i][0]
		if e<l:
			ans="NO"
			break
	print (ans)
