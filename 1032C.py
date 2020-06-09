n = int(input())
a = list(map(int,input().split()))
dp = [[0,1,2,3,4] for i in range(n+1)]
for i in range(2,n+1):
	if a[i-1]==a[i-2]:
		flag = -1
		for k in range(5):
			for j in range(5):
				if dp[i-1][j]!=-1 and j!=k:
					flag = j
					break
			if flag==-1:
				dp[i][k] = -1
			else:
				dp[i][k] = j
	elif a[i-1]>a[i-2]:
		dp[i][0] = -1
		for j in range(1,5):
			flag = -1
			for k in range(j):
				if dp[i-1][k]!=-1:
					flag = k
					break
			if flag==-1:
				dp[i][j] = -1
			else:
				dp[i][j] = k
	else:
		dp[i][4] = -1
		for j in range(4):
			flag = -1
			for k in range(j+1,5):
				if dp[i-1][k]!=-1:
					flag = k
					break
			if flag == -1:
				dp[i][j] = -1
			else:
				dp[i][j] = k
# for i in dp:
# 	print (*i)
flag = 0
for i in range(5):
	if dp[-1][i]!=-1:
		k = n
		j = i
		ans = [i+1]
		while k!=1:
			# print (k,j)
			ans.append(dp[k][j]+1)
			j = dp[k][j]
			k -= 1
		print (*(ans[::-1]))
		flag = 1
		break
if not flag:
	print (-1)