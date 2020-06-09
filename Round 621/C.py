from collections import Counter
s=input()
n=len(s)
if len(s)==1:
	print (1)
	exit()
if s.count(s[0])==len(s):
	print (max(len(s),(len(s)*(len(s)-1))//2))
	exit()
d=Counter(s)
l=[]
for i in d:
	l.append(d[i])
ans=max(l)
c={}
count={}
for i in range(n-1,-1,-1):
	if i==n-1:
		if s[i] not in count:
			count[s[i]]=1
		else:
			count[s[i]]+=1
	else:
		if s[i] not in count:
			count[s[i]]=1
		else:
			count[s[i]]+=1
		for j in d:
			if j in count and j!=s[i]:
				if s[i]+j not in c:
					c[s[i]+j]=count[j]
				else:
					c[s[i]+j]+=count[j]
for i in c:
	if c[i]>ans:
		ans=c[i]
for i in d:
	if (d[i]*(d[i]-1))//2>ans:
		ans=(d[i]*(d[i]-1))//2
print (ans)

