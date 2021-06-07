import sys
import math
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	e = 0
	b = []
	for i in a:
		if not i%2:
			e += 1
		else:
			if i!=1:
				b.append(i)
	ans = 0
	k = n-1
	for i in range(e):
		ans += k
		k -= 1
	c = {}
	for i in range(len(b)):
		for j in range(i+1, len(b)):
			if math.gcd(b[i], b[j])>1:
				ans += 1

	print (ans)

 
