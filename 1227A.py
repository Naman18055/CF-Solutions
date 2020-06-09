for nt in range(int(input())):
	n = int(input())
	a = []
	m1,m2 = 10**18,0
	for i in range(n):
		x = list(map(int,input().split()))
		if x[1]<m1:
			m1 = x[1]
			ind1 = i
		if x[0]>m2:
			m2 = x[0]
			ind2 = i
		a.append(x)
	print (max(m2-m1,0))

	