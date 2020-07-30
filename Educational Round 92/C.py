from collections import Counter
for nt in range(int(input())):
	s = list(input())
	n = len(s)
	c = Counter(s)
	m = 0
	for i in c:
		m = max(m,c[i])
	ans = min(n-2,n-m)
	count = {}
	numbers = "0123456789"
	for i in numbers:
		flag = False
		for j in range(n):
			if s[j]==i:
				found = {}
				flag = True
			elif flag:
				if s[j] not in found:
					found[s[j]] = 1
					if i+s[j] not in count:
						count[i+s[j]] = 1
					else:
						count[i+s[j]] += 1

	# print (n,count)
	m = 0
	for i in count:
		m = max(m,count[i])
	print (min(ans,n-2*m,n-2))