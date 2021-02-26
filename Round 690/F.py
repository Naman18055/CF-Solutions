import bisect

for nt in range(int(input())):
	n = int(input())
	a = []
	l,r = [], []
	for i in range(n):
		x = list(map(int,input().split()))
		a.append(x)
		l.append(x[0])
		r.append(x[1])
	l.sort()
	r.sort()
	minn = n
	for i in a:
		seg = i
		leave = bisect.bisect_left(r, i[0]) + (n - bisect.bisect(l, i[1]))
		# print (seg, leave)
		minn = min(minn, leave)
	print (minn)

