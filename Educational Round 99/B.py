for nt in range(int(input())):
	x = int(input())
	c = 0
	if x%2:
		for jump in range(1, x+1):
			c += jump
			if c>=x:
				v = jump
				break
		if c==x:
			print (v)
		elif (c-x)<v and (c-x)!=1:
			print (v)
		elif c==x+1:
			print (v+1)

	else:
		for jump in range(1, x+1):
			c += jump
			if c>=x:
				if c!=x+1:
					ans = jump
				else:
					ans = jump + 1
				break
		print (ans)