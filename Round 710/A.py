for nt in range(int(input())):
	n, m, x = map(int,input().split())
	print (((x-1)//n+1)+((x-1)%n)*m)