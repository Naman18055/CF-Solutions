s = input()
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]
count = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	dp[i][i] = 1
	count[i][i] = 1
for i in range(n-1,-1,-1):
	for j in range(i,n):
		if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
			dp[i][j] = 1
for i in range(1,n):
	for j in range(i-1,-1,-1):
		if j==i-1:
			if dp[j][i]:
				count[j][i] = 3
			else:
				count[j][i] = 2
		else:
			count[j][i] = count[j+1][i] + count[j][i-1] - count[j+1][i-1]
			if dp[j][i]:
				count[j][i] += 1
# for i in count:
	# print (*i)
for i in range(int(input())):
	l,r = map(int,input().split())
	print (count[l-1][r-1])