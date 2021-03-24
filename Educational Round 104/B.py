for nt in range(int(input())):
	n, k = map(int,input().split())
	if not n%2:
		print ((k-1)%n+1)
		continue
	
	k -= 1
	print ((k+(k//(n//2)))%n+1)