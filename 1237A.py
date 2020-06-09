import math
n = int(input())
a = []
b = []
for i in range(n):
	a.append(int(input()))
turn = 1
for i in range(n):
	if a[i]%2:
		if turn:
			b.append(math.floor(a[i]/2))
			turn = 0
		else:
			b.append(math.ceil(a[i]/2))
			turn = 1
	else:
		b.append(a[i]//2)
for i in b:
	print (i)