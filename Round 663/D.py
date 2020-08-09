import sys
input = sys.stdin.readline

def transpose():
	mat = [[0 for i in range(n)] for j in range(m)]
	for i in range(m): 
		for j in range(n): 
			mat[i][j] = inp[j][i]
	return mat

def count2(ind):
	return mat[ind].count("1")+mat[ind+1].count("1")

def calc(i):
	if i==0 or i==7:
		return [2,5]
	if i==2 or i==5:
		return [0,7]
	if i==1 or i==6:
		return [3,4]
	return [1,6]

def func(a,b):
	ans = 0
	a = bin(a)[2:]
	a = "0"*(n-len(a))+a
	for i in range(len(a)):
		if a[i]!=b[i]:
			ans += 1
	return ans


n,m = map(int,input().split())
inp = []
for i in range(n):
	inp.append("".join(input().strip()))
if n<m:
	mat = [''.join([inp[j][i] for j in range(n)]) for i in range(m)]
else:
	mat = inp
# print (mat)
n, m = min(n,m), max(n,m)
if n>=4 and m>=4:
	print (-1)
	exit()
if n==1:
	print (0)
	exit()

x = 2**n
dp = [[0 for i in range(x)] for j in range(m)]
for i in range(x):
	dp[0][i] = func(i,mat[0])
d = {0:[2,5],1:[3,4],2:[0,7],3:[1,6],4:[1,6],5:[0,7],6:[3,4],7:[2,5]}
d2 = {0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
for i in range(1,m):
	for j in range(x):
		if n==3:
			dp[i][j] = min(dp[i-1][d[j][0]],dp[i-1][d[j][1]])+func(j,mat[i])
		else:
			dp[i][j] = min(dp[i-1][d2[j][0]],dp[i-1][d2[j][1]])+func(j,mat[i])
# for i in mat:
	# print (*i)
# for i in dp:
	# print (*i)
ans = 10**18
for i in range(x):
	ans = min(ans,dp[-1][i])
print (ans)



