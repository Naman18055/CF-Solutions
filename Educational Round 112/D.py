import sys
input = sys.stdin.readline

n, m = map(int,input().split())
s = input()
a = ["abc", "acb", "bac", "bca", "cab", "cba"]
for i in range(6):
	a[i] = a[i]*(n//3)+a[i]*(n%3)
prefix = [[0 for i in range(n)] for j in range(6)]
for i in range(6):
	if a[i][0]!=s[0]:
		prefix[i][0] = 1
for i in range(6):
	for j in range(1, n):
		if s[j]!=a[i][j]:
			prefix[i][j] = prefix[i][j-1] + 1
		else:
			prefix[i][j] = prefix[i][j-1]

# for i in range(6):
# 	print (*prefix[i])
for i in range(m):
	l, r = map(int,input().split())
	minn = 10**18
	for i in range(6):
		if l!=1:
			minn = min(minn, prefix[i][r-1]-prefix[i][l-2])
		else:
			minn = min(minn, prefix[i][r-1])
	print (minn)

