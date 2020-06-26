for nt in range(int(input())):
	s = input()
	n = len(s)
	if "0" not in s or "1" not in s:
		print ("NET")
		continue
	stack = [s[0]]
	ans = 0
	for i in range(1,n):
		if len(stack)==0:
			stack.append(s[i])
		else:
			if s[i]!=stack[-1]:
				stack.pop()
				ans = 1-ans
			else:
				stack.append(s[i])
	if ans:
		print ("DA")
	else:
		print ("NET")