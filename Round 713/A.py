import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	print (a.index([min(a) if a.count(min(a))==1 else max(a)][0])+1)
