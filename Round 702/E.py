import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	b = list(map(int,input().split()))
	a = [[b[i], i] for i in range(n)]
	a.sort()
	a.append([0, -1])
	ans = [0]*n
	s = 0
	ind = -1
	for i in range(n):
		s += a[i][0]
		if s<a[i+1][0]:
			ans[a[i][1]] = 0
			ind = i
		# print (ind)

	for i in range(n-1, ind, -1):
		ans[a[i][1]] = 1

	res = []
	for i in range(n):
		if ans[i]:
			res.append(i+1)
	print (len(res))
	print (*res)

