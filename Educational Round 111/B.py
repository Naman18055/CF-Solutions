for nt in range(int(input())):
	n, a, b = map(int,input().split())
	s = input()
	if b>=0:
		print (n*a+n*b)
		continue
	ans = 1
	curr = s[0]
	for i in range(1, n):
		if s[i]!=curr:
			ans += 1
			curr = s[i]
	print (a*n+b*(ans//2+1))