for nt in range(int(input())):
	x, y = map(int,input().split())
	ans = 2*min(x, y)
	if x==y:
		print (ans)
	else:
		left = abs(x-y)
		ans += 2*(left-1) + 1
		print (ans)