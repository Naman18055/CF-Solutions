n=int(input())
l=list(map(int,input().split()))
ans=0
d={0:-1}
pref=0
ind=-1
for i in range(n):
	pref+=l[i]
	if pref in d:
		ind=max(ind,d[pref]+1)
	d[pref]=i
	ans+=(i-ind)
print (ans)