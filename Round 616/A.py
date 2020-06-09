for nt in range(int(input())):
	n=int(input())
	s=input()
	k=0
	for i in s:
		k+=int(i)
	ans=-1
	for i in range(n-1,-1,-1):
		if int(s[i])%2==1 and k%2==0:
			ans=i
			break
		else:
			k-=(int(s[i]))
	if ans==-1:
		print (-1)
	else:
		print (s[0:ans+1])
