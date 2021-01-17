for nt in range(int(input())):
	n = int(input())
	s = input()
	if "<" not in s or ">" not in s:
		print (n)
		continue
	ans = 0
	for i in range(n):
		if s[i]=="-" or s[i-1]=="-":
			ans += 1
			continue
	print (ans)