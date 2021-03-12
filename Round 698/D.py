import sys
input = sys.stdin.readline

import math
for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	ans = 0
	for i in range(1, n):
		ans = math.gcd(ans, a[i]-a[0])
	if (k-a[0])%ans==0:
		print ("YES")
	else:
		print ("NO")