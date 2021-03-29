def check(s):
	stack = []
	for i in s:
		if i==")":
			if not stack:
				return False
			stack.pop()
		else:
			stack.append("(")
	if stack:
		return False
	return True

for nt in range(int(input())):
	s = input()
	x = ["(", ")"]
	flag = False
	for i in x:
		for j in x:
			for k in x:
				new = ""
				for l in s:
					if l=="A":
						new += i
					elif l=="B":
						new += j
					else:
						new += k
				if check(new):
					flag = True
					break
			if flag:
				break
		if flag:
			break
	if flag:
		print ("YES")
	else:
		print ("NO")