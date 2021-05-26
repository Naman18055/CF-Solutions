import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = {}
	for i in range(n):
		if a[i] in c:
			c[a[i]].append(i)
		else:
			c[a[i]] = [i]

	ans = 0
	for i in c:
		pref = c[i][0]+1
		s = 0
		for j in range(1, len(c[i])):
			s += ((pref)*(n-c[i][j]))
			pref += (c[i][j]+1)
		ans += s
	print (ans)



	"""

	_, _, _, i, _, _, j, _, k, _, _ 
	[i, j, k]
	i*(n-j) +
	i*(n-k) + j*(n-k)


	"""