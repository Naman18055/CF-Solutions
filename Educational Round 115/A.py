for nt in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	t = []
	for i in range(n):
		if a[i]=="1":
			t.append([i, 1])
		if b[i]=="1":
			t.append([i, 2])
	t.sort()
	ans = "NO"
	for i in range(1, n):
		if (t[i][0]-t[i-1][0])**2 + (t[i][1]-t[i-1][1])**2<=2:
			ans = "YES"
			break
	print (ans)



