for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (0)
		continue
	c3, c2 = 0, 0
	m = n
	while n%3==0:
		n = n//3
		c3 += 1
	n = m
	while n%2==0:
		n = n//2
		c2 += 1
	if c2==c3:
		n = m
		ans = 0
		while n%6==0:
			n = n//6
			ans += 1
		if n==1:
			print (ans)
		else:
			print (-1)
	elif c3>c2:
		n = m
		for i in range(c3-c2):
			n = n*2
		ans = c3 - c2
		while n%6==0:
			n = n//6
			ans += 1
		if n==1:
			print (ans)
		else:
			print (-1)
	else:
		print (-1)