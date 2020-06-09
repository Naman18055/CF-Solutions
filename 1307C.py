from collections import Counter
s=input()
n=len(s)
c=Counter(s)
dp=[[0 for i in range(n)] for i in range(26)]
maxx2=[0]*n
loc={}
for i in range(n):
	if s[i] not in loc:
		loc[s[i]]=[i]
	else:
		loc[s[i]].append(i)
	for j in range(26):
		if ord(s[i])==j+97:
			dp[j][i]=dp[j][i-1]+1
		else:
			dp[j][i]=dp[j][i-1]

for i in range(n):
	m=0
	for j in range(26):
		m=max(m,dp[j][-1]-dp[j][i])
	maxx2[i]=m

ans=0
for i in c:
	ans=max(ans,c[i])
for i in loc:
	for j in range(26):
		m=0
		for k in loc[i]:
			m+=(dp[j][-1]-dp[j][k])
		ans=max(ans,m)
print (ans)