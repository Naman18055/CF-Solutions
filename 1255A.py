for nt in range(int(input())):
	a,b=map(int,input().split())
	a,b = min(a,b),max(a,b)
	print ((b-a)//5 + ((b-a)%5)//2 + ((b-a)%5)%2)