import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n,k,days = map(int,input().split())
	a = list(map(int,input().split()))
	d = {}
	for i in range(days):
		if a[i] not in d:
			d[a[i]] = 1
		else:
			d[a[i]] += 1
	ans = count = len(d)
	for i in range(days,n):
		if a[i] not in d:
			d[a[i]] = 1
			count += 1
		else:
			d[a[i]] += 1
		d[a[i-days]] -= 1
		if d[a[i-days]]==0:
			del d[a[i-days]]
			count -= 1
		ans = min(ans,count)
	print (ans)