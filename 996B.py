import math
n = int(input())
a = list(map(int,input().split()))
if n==1:
	print (1)
	exit()
if a[0]==0:
	print (1)
	exit()
dp = []
for i in range(n):
	if (a[i]-i)<=0:
		dp.append(0)
	else:
		dp.append(math.ceil((a[i]-i)/n))
# print (dp)
minn = dp[0]
ans = 1
for i in range(1,n):
	if dp[i]<minn:
		minn = dp[i]
		ans = i+1
print (ans)