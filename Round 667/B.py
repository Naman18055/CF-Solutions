for nt in range(int(input())):
	a,b,x1,y1,n = map(int,input().split())
	x,y = x1,y1
	if (a-x)+(b-y)<=n:
		print (x*y)
		continue
	diff = (a-x)+(b-y)-n
	if x>=y:
		x,diff = x+min(diff,a-x),diff-min(diff,a-x)
		y += diff
		a2 = (x*y)
	else:
		y,diff = y+min(diff,b-y),diff-min(diff,b-y)
		x += diff
		a2 = (x*y)

	x,y = x1,y1

	if a>b:
		b,n = b-min(n,b-y),n-min(n,b-y)
		a -= min(n,a-x)
		a1 = (a*b)
	elif a==b:
		if y>=x:
			a,n = a-min(n,a-x),n-min(n,a-x)
			b -= min(n,b-y)
			a1 = (a*b)
		else:
			b,n = b-min(n,b-y),n-min(n,b-y)
			a -= min(n,a-x)
			a1 = (a*b)
	else:
		a,n = a-min(n,a-x),n-min(n,a-x)
		b -= min(n,b-y)
		a1 = (a*b)

	print (min(a1,a2))