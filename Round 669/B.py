import sys
import math
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	d = {}
	for i in a:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	ans = [max(a)]
	curr = ans[0]
	d[ans[0]] -= 1
	if d[ans[0]] ==0 :
		del d[ans[0]]

	while d and curr!=1:
		m = 0
		e = -1
		for i in d:
			x = math.gcd(i,curr)
			if x>m:
				m = x
				e = i
		curr = m

		ans.append(e)
		d[e] -= 1
		if d[e]==0:
			del d[e]

	for i in d:
		ans.extend([i]*d[i])
		# ans.append(i)
	print (*ans)
