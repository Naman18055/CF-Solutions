for nt in range(int(input())):
	n = int(input())
	s = input()
	c = 0
	for i in range(n-1, -1, -1):
		if s[i]!=")":
			break
		c += 1
	if c>n//2:
		print ("Yes")
	else:
		print ("No")