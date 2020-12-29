for nt in range(int(input())):
	n = int(input())
	s = input()
	flag = 0
	if n%2:
		for i in range(0,n,2):
			if int(s[i])%2:
				flag = 1
				break
		if flag:
			print (1)
		else:
			print (2)
	else:
		for i in range(1,n,2):
			if int(s[i])%2==0:
				flag = 1
				break
		if flag:
			print (2)
		else:
			print (1)