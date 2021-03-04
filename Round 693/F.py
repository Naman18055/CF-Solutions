for nt in range(int(input())):
	input()
	n, m = map(int,input().split())
	block = []
	for i in range(m):
		x, y = map(int,input().split())
		block.append([y-1, x-1])
	block.sort()
	ans = "YES"

	if m%2:
		ans = "NO"
		print (ans)
		continue

	for i in range(0, m, 2):
		r, c = block[i][1], block[i][0]
		r1, c1 = block[i+1][1], block[i+1][0]

		if r==r1:
			if (c1-c)%2==0:
				ans = "NO"
				break
		else:
			if (c1-c)%2:
				ans = "NO"
				break

		if i!=0 and block[i-1][0]==c:
			ans = "NO"
			break

	print (ans)





