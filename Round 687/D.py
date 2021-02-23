import sys
input = sys.stdin.readline

def xor(n, m):
	ans = a[n]
	for i in range(n+1, m):
		ans = ans^a[i]
	return ans

n = int(input())
a = list(map(int,input().split()))
if n>80:
	print (1)
else:
	ans = 10**9
	for l in range(n-1):
		for r in range(l+1, n):
			for m in range(l, r):
				x = xor(l, m+1)
				y = xor(m+1, r+1)
				if y<x:
					ans = min(ans, r-l-1)
	if ans==10**9:
		print (-1)
	else:
		print (ans)