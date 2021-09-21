for nt in range(int(input())):
	l, r = map(int,input().split())
	if l>r//2:
		print (r%l)
		continue

	print (r%(r//2+1))


