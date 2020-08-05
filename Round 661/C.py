import sys
from collections import Counter
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	c = Counter(a)
	loc = {}
	for i in range(n):
		if a[i] not in loc:
			loc[a[i]] = [0,i]
		else:
			loc[a[i]].append(i)

	ans = 0
	for i in range(2,2*n+1):
		count = 0
		for j in c:
			if j>=i:
				continue
			if i-j in c:
				count += min(c[j],c[i-j])
		ans = max(ans,count)
	print (ans//2)

