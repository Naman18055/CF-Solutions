import sys
input = sys.stdin.readline

from collections import Counter
for nt in range(int(input())):
	n, k = map(int,input().split())
	a = input()
	b = input()
	c1 = Counter(a)
	c2 = Counter(b)
	ans = "YES"
	for i in range(26):
		if c2[chr(i+97)]>c1[chr(i+97)] or (c1[chr(i+97)] - c2[chr(i+97)])%k!=0:
			ans = "NO"
			break
		c1[chr(i+98)] += (c1[chr(i+97)]-c2[chr(i+97)])
	print (ans)