for nt in range(int(input())):
	n, s = map(int,input().split())
	if n==1:
		print (s)
		continue

	if n%2:
		print (s//((n-1)//2+1))
	else:
		print (s//(n//2+1))

