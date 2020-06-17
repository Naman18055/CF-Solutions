from collections import Counter
for nt in range(int(input())):
	s = list(input())
	c = Counter(s)
	s = list(set(s))
	n = len(s)
	s.sort(reverse=True)
	m = int(input())
	b = list(map(int,input().split()))
	j = 0
	ans = [-1]*m
	while b.count(-1)!=m:
		# print (b,j)
		x = b.count(0)
		while x>c[s[j]]:
			j += 1
		ind = []
		for i in range(m):
			if b[i]==0:
				ans[i] = s[j]
				b[i] = -1
				ind.append(i)
		for i in range(m):
			if b[i]>0:
				for k in ind:
					b[i] -= (abs(k-i))
		j += 1
	print ("".join(map(str,ans)))