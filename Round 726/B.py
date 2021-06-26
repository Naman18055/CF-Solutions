def Dist(a, b, x, y):
	return abs(i-a)+abs(j-b)+abs(x-a)+abs(y-b)+abs(x-i)+abs(y-j)

for nt in range(int(input())):
	n, m, i, j = map(int,input().split())
	if Dist(1, 1, n, m)<Dist(1, m, n, 1):
		print (1, 1, n, m)
	else:
		print (1, m, n, 1)