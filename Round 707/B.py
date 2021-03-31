import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	r = []
	for i in range(n):
		if a[i]:
			r.append([i-a[i]+1, i])
	if not r:
		print (*([0]*n))
		continue
	r.sort()
	ans = [1]*n
	curr = r[0][1]
	for i in range(r[0][0]):
		ans[i] = 0
	for i in range(1, len(r)):
		if r[i][0]<=curr:
			curr = max(curr, r[i][1])
		else:
			for j in range(curr+1, r[i][0]):
				ans[j] = 0
			curr = r[i][1]
	for i in range(curr+1, n):
		ans[i] = 0
	# print (r)
	print (*ans)

	