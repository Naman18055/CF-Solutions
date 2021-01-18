import sys
from collections import Counter
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if len(set(a))==1:
		print ("NO")
	else:
		print ("YES")
		c = Counter(a)
		m = 10**9
		for i in c:
			if c[i]<m:
				m = c[i]
				num = i
		d = {}
		for i in range(n):
			if a[i]==num:
				d[i] = 1
				x = i
		ans = []
		for i in range(n):
			if i not in d:
				ans.append((x+1, i+1))
		for i in range(n):
			if i not in d:
				for j in d:
					if j!=x:
						ans.append((i+1, j+1))
				break
		for i in ans:
			print (i[0], i[1])


