for nt in range(int(input())):
	w, h = map(int,input().split())
	x1, y1, x2, y2 = map(int,input().split())
	a, b = map(int,input().split())
	c, d = abs(x1-x2), abs(y1-y2)
	if a+c>w and b+d>h:
		print (-1)
		continue
	if a+c<=w and b+d<=h:
		ans = 10**18
		ans = min(ans, max(0, min(a-x1, b-y1)))
		ans = min(ans, max(0, min(a-(w-x2), b-y1)))
		ans = min(ans, max(0, min(a-(w-x2), b-(h-y2))))
		ans = min(ans, max(0, min(a-x1, b-(h-y2))))
		print (ans)
	elif a+c<=w:
		ans = 10**18
		ans = min(ans, max(0, min(a-x1, 10**18)))
		ans = min(ans, max(0, min(a-(w-x2), 10**18)))
		ans = min(ans, max(0, min(a-(w-x2), 10**18)))
		ans = min(ans, max(0, min(a-x1, 10**18)))
		print (ans)
	else:
		ans = 10**18
		ans = min(ans, max(0, min(10**18, b-y1)))
		ans = min(ans, max(0, min(10**18, b-y1)))
		ans = min(ans, max(0, min(10**18, b-(h-y2))))
		ans = min(ans, max(0, min(10**18, b-(h-y2))))
		print (ans)