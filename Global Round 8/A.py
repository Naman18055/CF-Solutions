for nt in range(int(input())):
	a,b,n = map(int,input().split())
	a,b = min(a,b),max(a,b)
	fib = [a,b]
	while fib[-1]<=n:
		fib.append(fib[-1]+fib[-2])
	# print (fib)
	print (len(fib)-2)