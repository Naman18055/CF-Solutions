t=int(input())
for nt in range(t):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	ans=[]
	counto=0
	for j in range(n):
		if l[j]%2==1:
			counto+=1
			ans.append(j+1)
	if counto<k:
		print ("NO")
	elif counto==k:
		print ("YES")
		for j in range(k-1):
			print (ans[j],end=" ")
		print (n)
	else:
		if k%2==1:
			if counto%2==0:
				print ("NO")
			else:
				print ("YES")
				ans[-1]=n
				ans=ans[::-1]
				ans=ans[:k]
				ans=ans[::-1]
				for i in ans:
					print (i,end=" ")
				print ()
		else:
			if counto%2==1:
				print ("NO")
			else:
				print ("YES")
				ans[-1]=n
				ans=ans[::-1]
				ans=ans[:k]
				ans=ans[::-1]
				for i in ans:
					print (i,end=" ")
				print ()