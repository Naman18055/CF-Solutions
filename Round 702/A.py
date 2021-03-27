import sys
import math
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	for i in range(1, n):
		ans += max(0, math.ceil(math.log2(max(a[i], a[i-1])/min(a[i], a[i-1])))-1)
	print (ans)

