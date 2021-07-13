for nt in range(int(input())):
	a, b = map(int,input().split())
	if a==b:
		print (0, 0)
		continue
	ans = abs(a-b)
	print (abs(a-b), min(a%(abs(a-b)), (abs(a-b) - a%(abs(a-b)))%abs(a-b)))