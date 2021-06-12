import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	minn, maxx = a.index(min(a)), a.index(max(a))
	minn, maxx = min(minn, maxx), max(minn, maxx)
	print (min(max(minn, maxx)+1, n - min(minn, maxx), minn + n - maxx + 1))