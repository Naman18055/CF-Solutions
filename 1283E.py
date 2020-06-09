n=int(input())
a=list(map(int,input().split()))
a.sort()
done={}
count=0
for i in range(n):
	if a[i]-1 not in done:
		done[a[i]-1]=1
		count+=1
	elif a[i] not in done:
		done[a[i]]=1
		count+=1
	elif a[i]+1 not in done:
		done[a[i]+1]=1
		count+=1
dp=[[1 for i in range(3)] for i in range(n)]
for i in range(1,n):
	if a[i]-1==a[i-1]:
		dp[i][0]=min(dp[i-1][1],min(dp[i-1][0],dp[i-1][2])+1)
		dp[i][1]=min(dp[i-1][2],min(dp[i-1][0],dp[i-1][2])+1)
	elif a[i]-1==a[i-1]+1:
		dp[i][0]=min(dp[i-1][2],min(dp[i-1][0],dp[i-1][2])+1)
		dp[i][1]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
	elif a[i]==a[i-1]:
		dp[i][0]=min(dp[i-1][0],min(dp[i-1][1],dp[i-1][2])+1)
		dp[i][1]=min(dp[i-1][1],min(dp[i-1][2],dp[i-1][0])+1)
		dp[i][2]=min(dp[i-1][2],min(dp[i-1][0],dp[i-1][1])+1)
		continue
	else:
		dp[i][0]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
		dp[i][1]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
	dp[i][2]=min(dp[i-1][0],dp[i-1][1],dp[i-1][2])+1
	# for i in dp:
	# 	print (*i)
	# print ()
print (min(dp[-1][0],dp[-1][1],dp[-1][2]),count)