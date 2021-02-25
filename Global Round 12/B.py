def dist(a, b):
	return abs(a[0]-b[0]) + abs(a[1]-b[1])

def check(i):
	for j in pt:
		if dist(j, i)>k:
			return False
	return True

for nt in range(int(input())):
	n,k = map(int,input().split())
	pt, x, y = [], [], []
	for i in range(n):
		pt.append(list(map(int,input().split())))
	ans = 0
	for i in pt:
		if check(i):
			ans = 1
			break
	if ans:
		print (ans)
	else:
		print (-1)


