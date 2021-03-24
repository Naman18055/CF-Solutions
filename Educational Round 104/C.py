for nt in range(int(input())):
	n = int(input())
	if n%2:
		turn = 1
		for i in range((n*(n-1))//2):
			print (turn, end=" ")
			turn = -turn
		print ()
		continue
	
	t = ((n*(n-1))//2)%n
	v = (((n*(n-1))//2)//n)*3+1
	c = [0]*n
	curr = 0
	while curr<n-1:
		for i in range(n-curr-1):
			if c[curr]==v:
				print (-1, end=" ")
				c[curr+i+1] += 3
			else:
				if v-c[curr]==1:
					print (0, end=" ")
					c[curr+i+1] += 1
					c[curr] += 1
				else:
					print (1, end=" ")
					c[curr] += 3
		curr += 1
	print ()
