for nt in range(int(input())):
	s=input()
	t=input()
	n=len(s)
	d=set(s)
	flag=0
	for i in t:
		if i not in d:
			print (-1)
			flag=1
			break
	if flag:
		continue
	dp=[[-1 for i in range(n)] for j in range(26)]
	for i in range(n-1,-1,-1):
		if i==n-1:
			dp[ord(s[i])-97][-1]=i
			continue
		for j in range(26):
			if ord(s[i])-97==j:
				dp[j][i]=i
			else:
				dp[j][i]=dp[j][i+1]
	# for i in dp:
	# 	print (*i)
	ans=1
	k=0
	for i in range(len(t)):
		if k>=n or dp[ord(t[i])-97][k]==-1:
			k=dp[ord(t[i])-97][0]+1
			ans+=1
		else:
			k=dp[ord(t[i])-97][k]+1
		# print (k,t[i])
	print (ans)
