import sys
from collections import Counter
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	minn = a[-1]
	for i in range(1, n):
		if a[i]-a[i-1]<minn:
			minn = a[i]-a[i-1]
			ind = i

	ans = [a[ind-1]]
	for i in range(ind+1, n):
		ans.append(a[i])
	for i in range(ind-1):
		ans.append(a[i])
	ans.append(a[ind])
	print (*ans)


