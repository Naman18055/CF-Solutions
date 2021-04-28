import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = []
	c = []
	for i in a:
		if i%2:
			b.append(i)
		else:
			c.append(i)
	print (*(b+c))