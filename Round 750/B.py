import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	z = a.count(0)
	o = a.count(1)
	print (o*(2**z))