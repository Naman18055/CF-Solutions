for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = ""
	for i in s:
		if i=="U":
			ans += "D"
		elif i=="D":
			ans += "U"
		else:
			ans += i
	print (ans)