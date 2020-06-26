import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	b.sort()
	a.sort(reverse=True)
	h = []
	for i in range(k):
		h.append([-1]*b[i])
	for i in range(k):
		h[i][0] = a[i]
	x = k
	for i in range(k):
		for j in range(1,b[i]):
			h[i][j] = a[x]
			x += 1
	# print (h)
	ans = 0
	for i in h:
		ans += (i[0]+i[-1])
	print (ans)
