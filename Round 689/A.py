for nt in range(int(input())):
	n, k = map(int,input().split())
	print ("abc"*(n//3)+"abc"[0:n%3])