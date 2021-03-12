from collections import Counter
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	maxx = 1
	for i in c:
		maxx = max(maxx, c[i])
	print (maxx)