import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10000)
def calc(i,sub):
	i=n-1
	while i>=0:
		if i==n-1:
			dp[i]=max(0,l[i][0]-l[i-1][1])
			i-=1
			continue
		if i==0:
			dp[i]=l[i][0]+dp[i+1]
			break
		if l[i-1][1]<l[i][0]:
			dp[i]=l[i][0]-l[i-1][1]+dp[i+1]
		elif l[i-1][1]>=l[i][0]:
			dp[i]=0+dp[i+1]
		i-=1

	# if i==n-1:
	# 	if sub>=l[i][0]:
	# 		return 0
	# 	else:
	# 		dp[i]=l[i][0]-sub
	# 		return dp[i]
	# if sub>=l[i][0]:
	# 	dp[i]=0+calc(i+1,l[i][1])
	# else:
	# 	dp[i]=(l[i][0]-sub)+calc(i+1,l[i][1])
	# return dp[i]

for nt in range(int(input())):
	n=int(input())
	l=[]
	dp=[]
	for i in range(n):
		temp=input().split()
		a=int(temp[0])
		b=int(temp[1])
		# a,b=map(int,input().split())
		l.append((a,b))
		dp.append(0)
	# dp=[0]*n
	calc(0,0)
	last=max(0,l[0][0]-l[-1][1])
	ans=dp[0]
	# print (dp,last)
	for i in range(1,n-1):
		a=(l[i][0]+dp[i+1]+last+dp[1]-dp[i])
		ans=min(ans,a)
		# print (a)
	ans=min(ans,l[-1][0]+last+dp[1]-dp[-1])
	print (ans)