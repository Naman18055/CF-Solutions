import math

for nt in range(int(input())):
	n = int(input())
	if n>8:
		ans = []
		k = n
		for i in range(9, n):
			ans.append( (i, n))
		while k!=1:
			ans.append( (n, 8))
			k = math.ceil(k/8)
		ans.append( (3, 8))
		for i in range(5, 8):
			ans.append( (i, 8))
		ans.append( (8, 4))
		ans.append( (8, 4))
		ans.append( (4, 2))
		ans.append( (4, 2))
	elif n>4:
		ans = []
		for i in range(3, n):
			if i!=4:
				ans.append( (i, n))
		ans.append( (n, 4))
		ans.append( (n, 4))
		ans.append( (4, 2))
		ans.append( (4, 2))
	elif n==3:
		ans = [(3, 2), (3, 2)]
	elif n==4:
		ans = [(3, 4), (4, 2), (4, 2)]
	print (len(ans))
	for i in ans:
		print (i[0], i[1])


