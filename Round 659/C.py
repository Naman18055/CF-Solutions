for nt in range(int(input())):
	n = int(input())
	s = list(input())
	t = input()
	new = []
	alpha = []
	for i in range(97,117):
		alpha.append(chr(i))
	flag = 0
	for i in range(n):
		if t[i]<s[i]:
			flag = 1
			break
	if flag:
		print (-1)
		continue
	ans = 0

	for i in range(97,117):
		x = "z"
		flag = 0
		for j in range(n):
			if s[j]==t[j]:
				continue
			if s[j]==chr(i):
				x = min(x,t[j])
				flag = 1
		if not flag:
			continue
		ans += 1
		for j in range(n):
			if s[j]==t[j]:
				continue
			if s[j]==chr(i):
				s[j] = x
		# print (s)
	print (ans)