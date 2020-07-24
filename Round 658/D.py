import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())*2
	a = list(map(int,input().split()))
	sub = []
	i = n-1
	while i>=0:
		m = max(a[0:i+1])
		j = i
		sub.append([m])
		while a[j]!=m:
			sub[-1].append(a[j])
			j -= 1
		# if not len(sub[-1]):
		# 	sub[-1].append(a[j])
		# else:
		# 	sub.append([a[j]])
		i = j-1
	new = []
	for i in sub:
		new.append(len(i))
	# print (sub)
	# print (new)

	dp = [[0 for i in range(n+1)] for j in range(len(new))]
	dp[0][new[0]] = 1
	for i in range(1,len(new)):
		dp[i][new[i]] = 1
		for j in range(n):
			if dp[i-1][j-new[i]] or dp[i-1][j]:
				dp[i][j] = 1
	# for i in dp:
		# print (*i)

	if dp[-1][n//2]:
		print ("YES")
	else:
		print ("NO")

