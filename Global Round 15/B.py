def diff(a, b):
	x = 0
	for i in range(5):
		if a[i]<b[i]:
			x += 1
	if x>=3:
		return False
	return True

for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	curr = 0
	for i in range(1, n):
		if diff(a[curr], a[i]):
			curr = i
	flag = True
	for i in range(n):
		if i!=curr:
			if diff(a[curr], a[i]):
				flag = False
	if flag:
		print (curr+1)
	else:
		print (-1)