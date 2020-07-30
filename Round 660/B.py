for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (8)
		continue
	m = (n-1)//4+1
	ans = ["9"]*n
	for i in range(n-1,n-m-1,-1):
		ans[i] = "8"
	print ("".join(map(str,ans)))
