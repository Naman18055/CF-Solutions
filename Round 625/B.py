n=int(input())
l=list(map(int,input().split()))
if n==1:
	print (l[0])
	exit()
d={}
for i in range(n):
	if l[i]-i not in d:
		d[l[i]-i]=[l[i]]
	else:
		d[l[i]-i].append(l[i])
ans=0
for i in d:
	if sum(d[i])>ans:
		ans=sum(d[i])
print (ans)