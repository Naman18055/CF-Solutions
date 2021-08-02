for nt in range(int(input())):
	n = int(input())
	s = list(input())
	a = sorted(s)
	count = 0
	for i in range(n):
		if s[i]==a[i]:
			count += 1
	print (n-count)