import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, k = map(int,input().split())
	h = list(map(int,input().split()))
	ans = "YES"
	minn = h[0]
	maxx = h[0]
	for i in range(1, n):
		minn = max(h[i], minn-k+1)
		maxx = min(h[i]+k-1, maxx+k-1)
		if maxx<minn or minn+k-1<maxx:
			ans = "NO"
			break
	if minn>h[-1] or h[-1]>maxx:
		ans = "NO"
	print (ans)



