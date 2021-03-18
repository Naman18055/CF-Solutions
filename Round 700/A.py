for nt in range(int(input())):
	s = input()
	turn = 1
	ans = ""
	for i in range(len(s)):
		if turn:
			if s[i]=="a":
				ans += "b"
			else:
				ans += "a"
		else:
			if s[i]=="z":
				ans += "y"
			else:
				ans += "z"
		turn = 1-turn
	print (ans)