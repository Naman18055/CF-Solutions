for nt in range(int(input())):
	a, b, c = map(int,input().split())
	n = (abs(a-b)-1)*2 + 2
	if c<=n//2:
		ans = n//2 + c
	else:
		ans = c - n//2
	if a<=n and b<=n and c<=n and ans<=n:
		print (ans)
	else:
		print (-1)
