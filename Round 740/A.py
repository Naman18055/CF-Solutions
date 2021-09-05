import sys
input = sys.stdin.readline

def odd(arr):
	for i in range(1, n, 2):
		if a[i-1]>a[i]:
			a[i], a[i-1] = a[i-1], a[i]

def even(arr):
	for i in range(2, n, 2):
		if a[i-1]>a[i]:
			a[i], a[i-1] = a[i-1], a[i]

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = sorted(a)
	i = 1
	count = 0
	while b!=a:
		if i%2:
			odd(a)
		else:
			even(a)
		i += 1
	print (i - 1)