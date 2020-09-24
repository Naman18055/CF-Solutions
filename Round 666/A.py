from collections import Counter
for nt in range(int(input())):
	n = int(input())
	a = ""
	for i in range(n):
		a+=input()
	c = Counter(a)
	ans = "YES"
	for i in c:
		if c[i]%n!=0:
			ans = "NO"
	print (ans)
