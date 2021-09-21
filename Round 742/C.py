def recur(i):
	if i<0:
		print ("".join(list(map(str, a))), "".join(list(map(str, b))))
		ans[0] += 1
		return 
	for o1 in range(10):
		for o2 in range(10):
			if (o1+o2+carry[i])%10==int(s[i]):
				# print (i, o1, o2, a, b)
				if (o1+o2+carry[i])//10!=0:
					if i-2>=0:
						x = (o1+o2+carry[i])//10
						carry[i-2] += x
						a[i] = o1
						b[i] = o2
						# print (o1, o2)
						recur(i-1)
						carry[i-2] -= x
				else:
					a[i] = o1
					b[i] = o2
					recur(i-1)


for nt in range(int(input())):
	n = int(input())
	s = str(n)
	if len(s)==1:
		print (n-1)
		continue
	if len(s)==2:
		if n==10:
			print (0)
		else:
			print ((n//10+1)*(n%10+1) - 2)
		continue

	a = [0]*len(s)
	b = [0]*len(s)
	ans = [0]
	for o1 in range(10):
		for o2 in range(10):
			# print (o1, o2)
			if (o1+o2)%10==n%10:
				carry = [0]*len(s)
				i = len(s)-1
				a[i] = o1
				b[i] = o2
				x = (o1+o2+carry[i])//10
				carry[i-2] += x
				recur(i-1)
				carry[i-2] -= x
	print (ans[0]-2)

