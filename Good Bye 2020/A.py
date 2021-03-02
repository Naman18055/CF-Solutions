import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	diff = []
	for i in range(n):
		for j in range(i+1, n):
			diff.append(abs(a[j]-a[i]))
	print (len(set(diff)))