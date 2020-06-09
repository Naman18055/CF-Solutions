def calc(l,start,end,left):
	arr=l[start:end+1]
	ans=max(arr)
	for i in range(left+1):
		ans = min(ans,max(arr[i],arr[len(arr)-left-1+i]))
	return ans

for nt in range(int(input())):
	n,m,k=map(int,input().split())
	l=list(map(int,input().split()))
	if m==1:
		print (max(l[0],l[-1]))
		continue
	if m>k+1:
		ans = -1
		for i in range(k+1):
			ans = max(ans,calc(l,i,n-1-k+i,m-k-1))
		print (ans)
	else:
		ans=-1
		for i in range(m):
			if l[i]>ans:
				ans=l[i]
		for i in range(n-1,n-1-m,-1):
			if l[i]>ans:
				ans=l[i]
		print (ans)
