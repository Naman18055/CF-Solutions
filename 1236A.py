for nt in range(int(input())):
	a,b,c = map(int,input().split())
	print (3*(min(b,c//2))+3*min(a,(b-min(b,c//2))//2))