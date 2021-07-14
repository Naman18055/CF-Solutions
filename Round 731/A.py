for nt in range(int(input())):
	input()
	a, b = map(int,input().split())
	x, y = map(int,input().split())
	f, g = map(int,input().split())
	if a==x and x==f and abs(y-g) + abs(g-b) == abs(y-b):
		print (abs(a-x)+abs(b-y)+2)
	elif b==y and y==g and abs(x-f) + abs(f-a) == abs(a-x):
		print (abs(a-x)+abs(b-y)+2)
	else:
		print (abs(a-x)+abs(b-y))

