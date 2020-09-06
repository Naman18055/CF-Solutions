for nt in range(int(input())):
	a,b = map(int,input().split())
	print ((abs(b-a)-1)//10+1)
