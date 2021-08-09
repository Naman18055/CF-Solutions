import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	m = max(a)
	print (m+(sum(a)-m)/(n-1))