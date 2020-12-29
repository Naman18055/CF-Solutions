for nt in range(int(input())):
	n = int(input())
	s = input()
	ans = 0
	c = 1
	for i in range(1,n):
		if s[i]==s[i-1]:
			ans += 1
			ans = min(ans, c)
		else:
			c += 1
	print (ans + (c-ans+1)//2)