def modify():
	s=""
	a=[]
	letters=set(["h","a","r","d"])
	for i in range(n):
		if s1[i] in letters:
			s+=s1[i]
			a.append(a1[i])
	return s,a

n = int(input())
s1 = input()
a1 = list(map(int,input().split()))
s,a = modify()
n = len(s)
if n==0:
	print (0)
	exit()
dp = [[10**9 for i in range(4)] for j in range(n+1)]
for i in range(4):
	dp[1][i] = 0
if s[0]=="h":
	dp[1][0] += a[0]
for i in range(2,n+1):
	# print(s,dp)
	if s[i-1]=="h":
		dp[i][0] = dp[i-1][0] + a[i-1]
		dp[i][1] = dp[i-1][1]
		dp[i][2] = dp[i-1][2]
		dp[i][3] = dp[i-1][3]
	elif s[i-1]=="a":
		dp[i][1] = min(dp[i-1][1] + a[i-1], dp[i-1][0])
		dp[i][0] = dp[i-1][0]
		dp[i][2] = dp[i-1][2]
		dp[i][3] = dp[i-1][3]
	elif s[i-1]=="r":
		dp[i][2] = min(dp[i-1][2] + a[i-1], dp[i-1][1])
		dp[i][1] = dp[i-1][1]
		dp[i][0] = dp[i-1][0]
		dp[i][3] = dp[i-1][3]
	else:
		dp[i][3] = min(dp[i-1][3] + a[i-1], dp[i-1][2])
		dp[i][1] = dp[i-1][1]
		dp[i][0] = dp[i-1][0]
		dp[i][2] = dp[i-1][2]
# print (dp)
print (dp[-1][3])