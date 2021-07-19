for nt in range(int(input())):
	n = int(input())
	s = 1
	ans = 1
	i = 3
	while s<n:
		ans += 1
		s += i
		i += 2
	print (ans)