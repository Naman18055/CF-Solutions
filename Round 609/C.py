n,k=map(int,input().split())
a=input()
print (n)
if True:
	ans=["0"]*n
	change=-1
	flag=-1
	for i in range(k):
		if i+k<n:
			if a[i]>a[i+k]:
				change=i
				flag=1
				break
			elif a[i]<a[i+k]:
				change=k-1
				flag=2
				break
			else:
				continue
		else:
			break
	#print (flag)
	if change!=-1:
		if flag==1:
			for i in range(k):
				ans[i]=a[i]
			for i in range(k,n):
				ans[i]=ans[i-k]
			# for i in range(change+1,n):
			# 	if i-k>=0:
			# 		ans[i]=ans[i-k]
			# 	else:
			# 		ans[i]=0
		else:
			for i in range(k-1):
				ans[i]=a[i]
			ans[change]=str(int(a[change])+1)
			for i in range(k,n):
				ans[i]=ans[i-k]
		for i in ans:
			print (str(i),end="")
		print ()
	else:
		print (a)



