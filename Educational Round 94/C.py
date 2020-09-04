for nt in range(int(input())):
	s = input()
	n = len(s)
	x = int(input())
	ans = [""]*n
	flag = 1
	for i in range(n):
		if s[i]=="0":
			if i-x>=0:
				if ans[i-x]=="1":
					flag = 0
					break
				ans[i-x] = "0"
			if i+x<n:
				if ans[i+x]=="1":
					flag = 0
					break
				ans[i+x] = "0"
		else:
			if i-x>=0:
				if ans[i-x]=="0":
					if i+x<n:
						if ans[i+x]=="0":
							flag = 0
							break
						else:
							ans[i+x]="1"
					else:
						flag = 0
						break
				else:
					ans[i-x] = "1"
			else:
				if i+x<n:
					if ans[i+x]=="0":
						flag = 0
						break
					else:
						ans[i+x] = "1"
				else:
					flag = 0
					break


	if flag:
		for i in range(n):
			if ans[i]=="":
				ans[i] = "0"
		print ("".join(map(str,ans)))
	else:
		print (-1)
