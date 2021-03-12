for nt in range(int(input())):
	n, d = map(int,input().split())
	a = list(map(int,input().split()))
	for i in a:
		if i>=10*d:
			print ("YES")
			continue

		ans = "NO"
		for x in range(i+1):
			for y in range(1, i+1):
				if d*y + 10*x==i:
					ans = "YES"
					break
		print (ans)
