for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	exp = []
	for i in range(m):
		b = list(map(float,input().split()))
		exp.append(b)
	if sorted(a)==a:
		print (1)
		continue
	for i in range(n-1, -1, -1):
		if i+1!=a[i]:
			ind = i+1
			break
	b = []
	for i in exp:
		if i[0]>=ind:
			b.append(i)
	ans = 0
	prev = 1
	for i in range(len(b)):
		ans += prev*b[i][1]
		prev = prev*(1-b[i][1])
	print (ans)