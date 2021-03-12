import sys
from collections import Counter
input = sys.stdin.readline


for nt in range(int(input())):
	n = int(input())
	a = sorted(list(map(int,input().split())))
	c = Counter(a)
	dp = [0 for i in range(250000)]
	for i in range(1, 250000):
		if i in c:
			dp[i] += c[i]
		for j in range(i*2, 250000, i):
			dp[j] = max(dp[j], dp[i])
	print (n-max(dp))





	