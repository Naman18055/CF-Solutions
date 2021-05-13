for nt in range(int(input())):
	n = int(input())
	s = input()
	if "*" not in s:
		print (0)
		continue

	suff = [0]*n
	if s[0]=="*":
		suff[0] = 1
	for i in range(1, n):
		if s[i]=="*":
			suff[i] = suff[i-1] + 1
		else:
			suff[i] = suff[i-1]
	total = s.count("*")

	start = False
	ans = 0
	v = 0
	for i in range(n):
		if s[i]=="*":
			if not start:
				start = True
			ans += (min(suff[i]-1, total-suff[i]+1)*v)
			v = 0
		else:
			if start:
				v += 1

	print (ans)
