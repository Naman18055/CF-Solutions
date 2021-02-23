from collections import Counter
for nt in range(int(input())):
	n,k = map(int,input().split())
	a = list(map(int,input().split()))
	ans = n
	for i in range(1, max(a)+1):
		j = 0
		c = 0
		while j<n:
			if a[j]!=i:
				j += k
				c += 1
			else:
				j += 1
		ans = min(ans, c)
	print (ans)