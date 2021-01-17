for nt in range(int(input())):
	x1, y1, x2, y2 = map(int,input().split())
	right = abs(x2 - x1)
	up = abs(y2-y1)
	if up:
		if right:
			print (right + up + 2)
		else:
			print (up)
	else:
		print (right)