for nt in range(int(input())):
	n=int(input())
	s=input()
	ans1=1
	ans2=s
	for i in range(2,n+1):
		if (n-i)%2==0:
			k=s[i-1:]+s[0:i-1][::-1]
		else:
			k=s[i-1:]+s[0:i-1]
		if k<ans2:
			ans2=k
			ans1=i
	print (ans2)
	print (ans1)