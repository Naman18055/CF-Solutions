for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	for i in range(1,n):
		ans += abs(a[i]-a[i-1])
	dec = max(abs(a[1]-a[0]), abs(a[-1]-a[-2]))
	for i in range(1, n-1):
		dec = max(dec, abs(a[i]-a[i-1])+abs(a[i]-a[i+1])-abs(a[i-1]-a[i+1]))
	print (ans-dec)