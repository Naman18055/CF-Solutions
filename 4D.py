import sys
input = sys.stdin.readline
n,w,h = map(int,input().split())
a = []
for i in range(n):
	x,y = map(int,input().split())
	if x>w and y>h:
		a.append([x,y,i+1])
a.sort()
n = len(a)
dp = [[1,i] for i in range(n)]
for i in range(1,n):
	for j in range(i):
		if a[j][0]<a[i][0] and a[j][1]<a[i][1]:
			if dp[j][0]+1>dp[i][0]:
				dp[i][0] = dp[j][0] + 1
				dp[i][1] = j
m = 0
for i in range(n):
	if dp[i][0]>m:
		m = dp[i][0]
		ind = i
print (m)
ans = []
while m:
	ans.append(a[ind][-1])
	m -= 1
	ind = dp[ind][1]
print (*(ans[::-1]))