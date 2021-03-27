a = []
for i in range(1, 10001):
	a.append(i**3)
a = set(a)

for nt in range(int(input())):
	n = int(input())
	i = 1
	ans = "NO"
	while n-i**3>0:
		if n-i**3 in a:
			ans = "YES"
			break
		i += 1
	print (ans)

