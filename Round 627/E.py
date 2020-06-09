def printit(matrix):
	for i in matrix:
		for j in i:
			print (j,end=" ")
		print ()

n,h,start,end=map(int,input().split())
l=list(map(int,input().split()))
dp=[[-1 for i in range(h)] for j in range(n)]
if l[0]>=start and l[0]<=end:
	dp[0][l[0]]=1
else:
	dp[0][l[0]]=0
if l[0]-1>=start and l[0]-1<=end:
	dp[0][l[0]-1]=1
else:
	dp[0][l[0]-1]=0
#printit(dp)
for i in range(1,n):
	for j in range(h):
		time1=j+h-l[i]
		time2=j+h-l[i]+1
		if time1>=h:
			time1-=h
		if time2>=h:
			time2-=h
		# print (time1,time2)
		dp[i][j]=max(dp[i-1][time1],dp[i-1][time2])
		if dp[i-1][time1]!=-1 or dp[i-1][time2]!=-1:
			if j>=start and j<=end:
				dp[i][j]+=1

#printit(dp)
ans=0

# for i in range(n):
# 	for j in range(start,end+1):
# 		if dp[i][j]==1:
# 			ans+=1
# 			break

# for i in range(start,end+1):
# 	count=0
# 	for j in range(n):
# 		if dp[j][i]==1:
# 			count+=1
# 	if count>ans:
# 		ans=count

for i in range(start,end+1):
	for j in range(n):
		if dp[j][i]>ans:
			ans=dp[j][i]

print (ans)