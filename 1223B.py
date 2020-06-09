for nt in range(int(input())):
	a = input()
	b = input()
	a = set(list(a))
	b = set(list(b))
	flag = 0
	for i in a:
		if i in b:
			flag = 1
			break
	for i in b:
		if i in a:
			flag = 1
			break
	if not flag:
		print ("NO")
	else:
		print ("YES")