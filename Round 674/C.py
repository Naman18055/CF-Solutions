for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (0)
		continue
	ans = 10**18
	for i in range(max(1,int(n**0.5)-5),min(n,int(n**0.5)+5)):
		ans = min(ans, ((n-1)//i)+(i-1))
	print (ans)