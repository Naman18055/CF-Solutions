import math
def calc(a):
	n=len(a)
	m=len(a[0])
	dp=[[0 for i in range(m)] for j in range(n)]
	dp[0][0]=a[0][0]
	for i in range(n):
		for j in range(m):
			if  i==0 and j==0:
				continue
			if i!=0 and j!=0:
				dp[i][j]=max(dp[i-1][j]&a[i][j],dp[i][j-1]&a[i][j])
			elif i==0:
				dp[i][j]=dp[i][j-1]&a[i][j]
			else:
				dp[i][j]=dp[i-1][j]&a[i][j]
	print (dp)
	return dp[i][j]

k=int(input())
if k==0:
	print (1,1)
	print (2)
else:
	# matrix=[[26423,3,3,0],[4,0,3,0],[4,4,26423,3]]
	# print (calc(matrix))
	x=math.floor(math.log(k,2))+1
	y=2**x
	z=k
	print (4,4)
	ans=[[262143,z,z,0],[y,0,z,0],[y,0,z,0],[y,y,262143,z]]
	for i in ans:
		print (*i)
	# print (calc(ans))

# for i in range(1,100001):
# 	flag=False
# 	x=math.floor(math.log(i,2))+1
# 	y=2**x
# 	z=i
# 	if (z-(y&z))!=i:
# 		print (i,x,y,z,y-(y&z))
# 		break
	# for j in range(300000):
	# 	for k in range(j,300000):
	# 		if j-(k & j)==i:
	# 			print ("value of k : ",i)
	# 			print (j,k)
	# 			flag=True
	# 			break
	# 	if flag:
	# 		break