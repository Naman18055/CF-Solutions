import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, x = map(int,input().split())
	a = list(map(int,input().split()))
	maxx, minn = 0, 0
	minn = (sum(a)-1)//x + 1
	for i in a:
		maxx += (i-1)//x+1
	print ( minn, maxx)
