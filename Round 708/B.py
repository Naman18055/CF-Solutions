for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	b = {}
	for i in range(m):
		b[i] = 0
	ans = 0
	for i in a:
		b[i%m] += 1
	if b[0]:
		ans += 1
	if m%2==0 and b[m//2]:
		ans += 1
	# print (b, ans)
	for i in range(1, (m+1)//2):
		if min(b[i], b[m-i]):
			ans += max(0, max(b[i], b[m-i]) - min(b[i], b[m-i]) - 1)
			ans += 1
		else:
			ans += max(b[i], b[m-i])
	print (ans)