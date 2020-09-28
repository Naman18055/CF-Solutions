import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	minn = {}
	maxx = {}
	prev = {}
	for i in range(n):
		prev[a[i]] = 0
		maxx[a[i]] = 0
	for i in range(1,n+1):
		diff = i - prev[a[i-1]]
		maxx[a[i-1]] = max(maxx[a[i-1]],diff)
		prev[a[i-1]] = i
	for i in set(a):
		diff = n+1 - prev[i]
		maxx[i] = max(maxx[i],diff)

	f = 10**18
	for i in maxx:
		if maxx[i] in minn:
			minn[maxx[i]] = min(minn[maxx[i]],i)
		else:
			minn[maxx[i]] = i
		f = min(f, maxx[i])
	# print (maxx)
	# print (minn)

	ans = [-1]*n
	curr = minn[f]
	for i in range(f,n+1):
		if i not in minn:
			ans[i-1] = curr
			continue
		curr = min(curr, minn[i])
		ans[i-1] = curr
	print (*ans)
