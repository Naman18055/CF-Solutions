import sys
input = sys.stdin.readline

for nt in range(int(input())):
	a, b, c = map(int,input().split())
	s = a + 2*b + 3*c
	if s%2:
		print (1)
	else:
		print (0)