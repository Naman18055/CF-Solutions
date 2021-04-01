import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = sorted(list(map(int,input().split())))
	b = sorted(list(set(a)))
	for i in range(1, n):
		if a[i]==a[i-1]:
			b.append(a[i])
	print (*b)