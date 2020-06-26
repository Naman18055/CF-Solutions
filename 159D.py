def ispalindrome(s):
	if s==s[::-1]:
		return True
	return False

s = input()
n = len(s)
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	dp[i][i] = 1
for i in range(1,n):
	for j in range(i-1,-1,-1):
		if s[i]==s[j] and (j+1>i-1 or dp[j+1][i-1]):
			dp[j][i] = 1
pref = [0]*n
suff = [0]*n
pref[0] = suff[-1] = 1
for i in range(1,n):
	# pref[i] = pref[i-1]
	for j in range(i,-1,-1):
		if dp[j][i]:
			pref[i] += 1
for i in range(n-2,-1,-1):
	suff[i] = suff[i+1]
	for j in range(i,n):
		if dp[i][j]:
			suff[i] += 1

# for i in dp:
# 	print (*i)
# print (pref)
# print (suff)

ans = 0
curr = 0
for i in range(n-1):
	ans += suff[i+1]*pref[i]
print (ans)
 