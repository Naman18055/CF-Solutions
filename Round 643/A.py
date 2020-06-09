for nt in range(int(input())):
	n,k=map(int,input().split())
	for i in range(k-1):
		n+=(int(min(list(str(n))))*(int(max(list(str(n))))))
		if "0" in str(n):
			break
	print (n)