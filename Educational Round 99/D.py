import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	found = 0
	ans = 0
	# for i in range(n-1, -1, -1):
	# 	if a[i]<x and not found:
	# 		found = i
	# 		break
	# if sorted(a[0:found+1])!=a[0:found+1]:
	# 	print (-1)
	# 	continue

	# a = a[found+1:]
	# n = len(a)
	for i in range(n):
		if sorted(a)==a:
			break
		if a[i]>x:
			a[i], x = x, a[i]
			ans += 1
	if sorted(a)==a:
		print (ans)
	else:
		print (-1)
