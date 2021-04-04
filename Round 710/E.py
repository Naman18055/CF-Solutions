import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	minn = [0]*n
	minn[0] = a[0]
	for i in range(1, n):
		if a[i]!=a[i-1]:
			minn[i] = a[i]
	s = set(minn)
	curr = 1
	for i in range(n):
		if minn[i]==0:
			while curr in s:
				curr += 1
			minn[i] = curr
			curr += 1
	print (*minn)

	maxx = [0]*n
	maxx[0] = a[0]
	for i in range(1, n):
		if a[i]!=a[i-1]:
			maxx[i] = a[i]
	s = set(maxx)
	curr = n
	left = []
	prev = 0
	for i in range(n):
		if maxx[i]==0:
			maxx[i] = left.pop()
		else:
			for j in range(prev+1, maxx[i]):
				left.append(j)
			prev = maxx[i]
		# print (left)


	print (*maxx)



