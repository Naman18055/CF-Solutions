a = []
for i in range(20):
	a.append(3**i)
a = a[::-1]
for nt in range(int(input())):
	n = int(input())
	s = sum(a)
	for i in a:
		if s-i>=n:
			s -= i
	print (s)