import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k,l = map(int,input().split())
	d = list(map(int,input().split()))
	if max(d)>l:
		print ("No")
		continue
	dp = [[0 for i in range(2*k)] for j in range(n)]
	for i in range(k):
		if (d[0] + i)<=l:
			dp[0][i] = 1
	for i in range(k,2*k):
		if d[0]+(2*k-i)<=l:
			dp[0][i] = 1

	for i in range(1,n):
		for j in range(k):
			if (d[i]+j)<=l and (dp[i-1][j-1] or dp[i][j-1]):
				dp[i][j] = 1
		for j in range(k,2*k):
			if d[i]+(2*k-j)<=l and (dp[i-1][j-1] or dp[i][j-1]):
				dp[i][j] = 1

		# for i in dp:
		# 	print (*i)
		# print ()

	if 1 in dp[-1]:
		print ("Yes")
	else:
		print ("No")