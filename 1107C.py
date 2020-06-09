def cal(array,k):
	temp2=0
	ans=0
	while temp2<k:
		ans+=array[temp2]
		temp2+=1
	return ans

n,k=map(int,input().split())
l=list(map(int,input().split()))
s=input()
i=0
j=0
ans=0
while j<n:
	if s[i]==s[j]:
		j+=1
	else:
		if j-i+1<=k:
			ans+=sum(l[i:j])
			i=j
		else:
			temp=l[i:j]
			temp.sort(reverse=True)
			ans+=cal(temp,k)
			i=j
if n-i<k:
	ans+=sum(l[i:-1])
else:
	temp=l[i:-1]
	temp.sort(reverse=True)
	ans+=cal(temp,k)
print (ans)