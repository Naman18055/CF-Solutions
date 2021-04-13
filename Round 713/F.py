for nt in range(int(input())):
	n, c = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	ans = (c-1)//a[0]+1
	d = (b[0]-1)//a[0]+1
	p = d*a[0]
	for i in range(1, n):
		# print (p, d)
		p -= b[i-1]
		d += 1
		ans = min(ans, d+(c-p-1)//a[i]+1)
		# print (ans)
		if i==n-1:
			break
		d += (b[i]-p-1)//a[i]+1
		p += ((b[i]-p-1)//a[i]+1)*a[i]
	print (ans)