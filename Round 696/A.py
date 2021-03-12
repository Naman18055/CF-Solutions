for nt in range(int(input())):
	n = int(input())
	a = input()
	prev = -1
	ans = ""
	for i in a:
		if i=="1":
			if prev!=2:
				ans += "1"
				prev = 2
			else:
				ans += "0"
				prev = 1
		else:
			if prev!=1:
				ans += "1"
				prev = 1
			else:
				ans += "0"
				prev = 0
	print (ans)