import sys
input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	n = int(input())
	a = list_input()
	for i in range(n):
		a[i] -= 1
	dp = [[0 for i in range(200)] for i in range(n)]
	for i in range(n):
		for j in range(200):
			dp[i][j] = dp[i - 1][j]
		dp[i][a[i]] += 1

	m = 1
	for i in range(200):
		s, e, c = 0, n - 1, 0
		while s < e:
			while s < e and a[s] != i:
				s += 1
			while s < e and a[e] != i:
				e -= 1
			if s < e:
				c += 2
				for j in range(200):
					m = max(m, c + dp[e - 1][j] - dp[s][j])
				s += 1
				e -= 1
	print(m)
