for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	ans = a[-1]-a[0]
	for i in range(1,n):
		ans = min(ans, a[i]-a[i-1])
	print (ans)