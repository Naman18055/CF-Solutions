for nt in range(int(input())):
	n = int(input())
	a = [i for i in range(1,n+1)]
	ans = []
	while len(a)!=1:
		x = a.pop()
		y = a.pop()
		a.append((x+y-1)//2+1)
		ans.append([x,y])
	print (a[0])
	for i in ans:
		print (*i)