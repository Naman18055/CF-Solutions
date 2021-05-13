for nt in range(int(input())):
	n = int(input())
	s = input()
	a = [s[0]]
	for i in range(1, n):
		if s[i]==a[-1]:
			continue
		a.append(s[i])
	d = {}
	ans = "YES"
	for i in a:
		if i in d:
			ans = "NO"
			break
		else:
			d[i] = 1
	print (ans)