for nt in range(int(input())):
	n = int(input())
	if n%2:
		print (-1)
	else:
		ans = ""
		k = n
		while True:
			ans += "1"
			k = k-2
			i  = 2
			if not k:
				print (len(ans))
				print (" ".join(list(ans)))
				break
			while 2**i<k:
				ans += "0"
				k -= 2**i
				i += 1


