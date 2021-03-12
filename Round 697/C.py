from collections import Counter
for nt in range(int(input())):
	n, m, k = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	c1 = Counter(a)
	c2 = Counter(b)
	ans = 0
	for i in range(k):
		ans += (k-c1[a[i]]-c2[b[i]]+1)
	print (ans//2)