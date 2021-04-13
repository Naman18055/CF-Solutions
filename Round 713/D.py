import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	if sum(a[:-2]) == a[-1] or sum(a[:-2]) == a[-2]:
		print (*a[:-2])
		continue
	if sum(a[:-1])-a[-1] in a[:-1]:
		x = a[:-1].index(sum(a[:-1])-a[-1])
		print (*(a[0:x]+a[x+1:-1]))
		continue
	print (-1)
