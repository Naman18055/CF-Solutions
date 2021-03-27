import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = {0: 0, 1:0, 2:0}
	for i in a:
		c[i%3] += 1

	print (max(c[0]-c[2], c[1]-c[0], c[2]-c[1]))
