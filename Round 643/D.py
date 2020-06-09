n,s=map(int,input().split())
if n==1:
	if s==1:
		print ("NO")
	else:
		print ("YES")
		print (s)
		print (s//2)
	exit()
if n==s or n==s+1:
	print ("NO")
	exit()
k=s-n+1
r=[n,k-1]
if k-1<n:
	print ("NO")
elif k-1==n:
	if 2*n==s:
		print ("YES")
		ans=[1]*(n-1)
		ans.append(k)
		print (*ans)
		print (k-1)
	else:
		print ("NO")
else:
	print ("YES")
	ans=[1]*(n-1)
	ans.extend([k])
	print (*ans)
	print (k-1)
