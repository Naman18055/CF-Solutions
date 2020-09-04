import sys
from collections import Counter
input = sys.stdin.readline

def calc(a):
	return (a*(a-1)*(a-2)*(a-3))//24

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	left = [0]*(n+1)
	complete = [0]*(n+1)
	for i in a:
		complete[i] += 1
	ans = 0
	for i in range(n):
		b = left[::]
		c = complete[::]
		t = 0
		for j in range(i+1,n):
			if a[j]!=a[i]:
				c[a[j]] -= 1
				b[a[j]] += 1
				if b[a[j]]!=0 and c[a[j]]!=0:
					t -= ((b[a[j]]-1)*(c[a[j]]+1))
					t += b[a[j]]*c[a[j]]
				elif c[a[j]]==0:
					t -= (b[a[j]]-1)
			else:
				ans += t
			# print (b,c,t)
		# print (t)
		complete[a[i]] -= 1
	c = Counter(a)
	for i in c:
		if c[i]>=4:
			ans += calc(c[i])

	print (ans)

