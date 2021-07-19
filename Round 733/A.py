for nt in range(int(input())):
	n = input()
	ans = 0
	while n and int(n):
		s = len(n)
		new = ""
		for i in range(1, s):
			if n[i]<=n[0]:
				new += "0"
			else:
				new += str(int(n[i])-int(n[0]))
		ans += int(n[0])
		n = new
	print (ans)