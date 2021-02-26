for nt in range(int(input())):
	n = int(input())
	if n>45:
		print (-1)
	else:
		if n<=9:
			print (n)
			continue
		ans = []
		num = 9
		s = 0
		while s+num<n:
			s += num
			ans.append(num)
			num -= 1
		ans.append(n-s)
		ans.sort()
		print ("".join(map(str, ans)))
