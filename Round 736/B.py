for nt in range(int(input())):
	n = int(input())
	a = list(input())
	b = list(input())
	ans = 0
	for i in range(n):
		if i==0:
			if b[i]=="1":
				if a[i]=="0":
					ans += 1
				elif a[i+1]=="1":
					ans += 1
					a[i+1] = -1
			continue

		if b[i]=="1":
			if a[i]=="0":
				ans += 1
			elif a[i-1]=="1":
				ans += 1
			elif i<n-1 and a[i+1]=="1":
				ans += 1
				a[i+1] = -1

		# print (a)
		# print (b)
		# print ()

	print (ans)