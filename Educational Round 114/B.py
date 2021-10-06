for nt in range(int(input())):
	a, b, c, m = map(int,input().split())
	x = sorted([a, b, c])
	if m<=(a-1+b-1+c-1) and m>=x[2]-x[0]-x[1]-1:
		print("YES")
	else:
		print ("NO")