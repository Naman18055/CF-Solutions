for nt in range(int(input())):
	s = input()
	stack = []
	for i in range(len(s)):
		if not stack:
			stack.append(s[i])
			continue
		if s[i]=="B":
			stack.pop()
		else:
			stack.append(s[i])
	print (len(stack))