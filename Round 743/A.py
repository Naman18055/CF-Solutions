for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = 0
	for i in range(n-1):
		if s[i]!="0":
			ans += int(s[i]) + 1
	ans += int(s[-1])
	print (ans)