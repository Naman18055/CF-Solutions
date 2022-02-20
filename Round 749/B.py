for nt in range(int(input())):
	n, m = map(int,input().split())
	a = []
	for i in range(m):
		a.append(list(map(int,input().split())))
	done = [0]*n
	for i in a:
		done[i[1]-1] = 1
	for i in range(n):
		if not done[i]:
			root = i+1
	for i in range(1, n+1):
		if i!=root:
			print (i, root)
	
