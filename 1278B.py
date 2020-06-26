for nt in range(int(input())):
	a,b = map(int,input().split())
	if a==b:
		print (0)
		continue
	x = 1
	i = 1
	d = abs(a-b)
	while x<d or x%2!=d%2:
		i += 1
		x = (i*(i+1))//2
	print (i)
