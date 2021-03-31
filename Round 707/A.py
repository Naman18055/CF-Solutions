for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split())))
	a.append([0, 0])
	b = list(map(int,input().split()))
	p = 0
	for i in range(n-1):
		arr = (a[i][0]-a[i-1][1])+b[i]+p
		p = max(a[i][1], arr+(a[i][1]-a[i][0]-1)//2+1)
		# print (arr, p)
	print (p+b[-1]+(a[n-1][0]-a[n-2][1]))
