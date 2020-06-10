for nt in range(int(input())):
	n,k = map(int,input().split())
	flag = 0
	if k%3==0:
		x = n%(k+1)
		if x%3==0 and x!=k:
			flag = 1
	else:
		x = n%3
		if x==0:
			flag = 1
	if flag:
		print ("Bob")
	else:
		print ("Alice")