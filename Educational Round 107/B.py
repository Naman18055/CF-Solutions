for nt in range(int(input())):
	a, b, c = map(int,input().split())
	hcf = 10**(c-1)
	ans1 = "1"+"0"*(a-1)
	ans2 = "1"*(b-c+1)+"0"*(c-1)
	print (ans1, ans2)
