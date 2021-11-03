import sys
input = sys.stdin.readline

for nt in range(int(input())):
	k, n = map(int,input().split())
	a = sorted(list(map(int,input().split())))
	t = 0
	c = 0
	for i in a[::-1]:
		if t>=i:
			break
		t += (k-i)
		c += 1
	print (c)
	