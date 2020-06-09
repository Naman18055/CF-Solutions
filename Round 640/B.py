for nt in range(int(input())):
	n,k=map(int,input().split())
	if k>n:
		print ("NO")
		continue
	if k==n:
		print ("YES")
		ans=[1]*k
		print (*ans)
		continue
	if n%2 and k%2==0:
		print ("NO")
		continue
	if (n-k+1)%2:
		print ("YES")
		ans=[1]*(k-1)
		ans.append(n-k+1)
		print (*ans)
	else:
		if n%2==0 and k%2:
			# print (n-(k-1)*2)
			if (n-((k-1)*2))>=2 and (n-((k-1)*2))%2==0:
				print ("YES")
				ans=[2]*(k-1)
				ans.append(n-(2*(k-1)))
				print (*ans)
			else:
				print ("NO")
