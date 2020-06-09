for nt in range(int(input())):
	a=list(map(int,input().split()))
	x=list(map(int,input().split()))
	flag = 0
	if x[0]==a[0]:
		if x[1]+a[1]==x[0]:
			flag = 1
	if x[0]==a[1]:
		if x[1]+a[0]==x[0]:
			flag = 1
	if x[1]==a[0]:
		if x[0]+a[1]==a[0]:
			flag = 1
	if x[1]==a[1]:
		if x[0]+a[0]==a[1]:
			flag = 1
	if flag:
		print ("Yes")
	else:
		print ("No")
