for nt in range(int(input())):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	if a.count(x)==n:
		print (0)
		continue
	a.sort()
	diff = 0
	for i in range(n-1):
		diff += (x-a[i])
	if diff + x-a[-1] == 0 or x in a:
		print (1)
	else:
		print (2)