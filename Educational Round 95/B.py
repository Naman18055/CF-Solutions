import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	c = []
	for i in range(n):
		if b[i]!=1:
			c.append(a[i])
	ans = []
	j = 0 
	c.sort(reverse=True)
	for i in range(n):
		if b[i]==0:
			ans.append(c[j])
			j += 1
		else:
			ans.append(a[i])
	print (*ans)