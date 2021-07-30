for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append([input()])
	for i in range(n):
		c = {"a":0, "b":0, "c":0, "d":0, "e":0}
		for j in a[i][0]:
			c[j] += 1
		for j in c:
			a[i].append(2*c[j]-len(a[i][0]))
	ans = 0
	for i in range(5):
		a.sort(key = lambda x: x[i+1], reverse=True)
		# print (a)
		count = 0
		s = 0
		for j in range(n):
			s += a[j][i+1]
			if s<=0:
				break
			count += 1
		ans = max(ans, count)
	print (ans)


