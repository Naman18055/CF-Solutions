import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, k = map(int,input().split())
	a = list(map(int,input().split()))
	b = [a[i] for i in range(n)]
	b.sort()
	loc = {}
	for i in range(n):
		loc[b[i]] = i
	for i in range(n):
		a[i] = loc[a[i]]
	count = 1
	for i in range(1, n):
		if a[i]!=a[i-1]+1:
			count += 1
	# print (a, count)
	if count<=k:
		print ("Yes")
	else:
		print ("No")


	
	