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

	a = b = ""
	for i in range(len(s)):
		if i%2:
			a += s[i]
		else:
			b += s[i]
	a = int(a)
	b = int(b)
	print ((a+1)*(b+1)-2)

