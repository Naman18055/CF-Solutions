import sys
input = sys.stdin.readline


for nt in range(int(input())):
	n, q = map(int,input().split())
	s = input()
	a = []
	for i in range(n):
		if i%2:
			if s[i]=="+":
				a.append(-1)
			else:
				a.append(1)
		else:
			if s[i]=="+":
				a.append(1)
			else:
				a.append(-1)

	p = [0]
	for i in range(n):
		p.append(p[-1]+a[i])

	for i in range(q):
		l, r = map(int,input().split())
		if p[r]-p[l-1]==0:
			print (0)
			continue
		if (r-l+1)%2:
			print (1)
		else:
			print (2)
