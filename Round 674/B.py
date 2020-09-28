for nt in range(int(input())):
	n,m = map(int,input().split())

	tiles = []
	ans = "NO"
	for i in range(n):
		a = []
		a.append(list(map(int,input().split())))
		a.append(list(map(int,input().split())))
		tiles.append(a)
		if a[0][1]==a[1][0]:
			ans = "YES"
	if m%2:
		print ("NO")
		continue
	print (ans)