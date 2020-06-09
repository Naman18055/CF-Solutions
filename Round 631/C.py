n,m=map(int,input().split())
new=list(map(int,input().split()))
l=[]
for i in range(m):
	l.append((new[i],i))
l.sort(reverse=True)
ans=[-1]*m
ans[l[0][1]]=1
start=l[0][0]+1
left=-1
width=[l[0][0]]
for i in range(1,m):
	if start>n:
		left = m-i
		break
	ans[l[i][1]]=(min(start,n))
	width.append(min(l[i][0],n-start+1))
	start+=l[i][0]
if start>=n:
	if left==-1:
		print (*ans)
	else:
		# find=-1
		# print (*ans)
		# print (width,left)
		# print (left)
		flag = False
		start=2
		for i in range(m-left,m):
			if start<=(n-l[i][0]+1):
				ans[l[i][1]]=start
				start+=1
			else:
				flag=True
				break
		if flag:
			print (-1)
		else:
			print (*ans)
else:
	print (-1)