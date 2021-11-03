import sys
import math
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	m = min(a)
	b = []
	for i in range(n):
		if a[i]!=m:
			b.append(abs(a[i]-m))
	if not b:
		print (-1)
		continue
	ans = b[0]
	for i in range(1, len(b)):
		ans = math.gcd(ans, b[i])
	print (ans)

