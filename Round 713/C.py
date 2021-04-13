for nt in range(int(input())):
	a, b = map(int,input().split())
	s = list(input())
	n = a+b
	if a%2 and b%2:
		print (-1)
		continue
	flag = False
	for i in range(n//2):
		if s[i]=="?" and s[n-i-1]=="?":
			continue
		if s[i]=="?":
			s[i] = s[n-i-1]
		elif s[n-i-1]=="?":
			s[n-i-1] = s[i]
		else:
			if s[i]!=s[n-i-1]:
				flag = True
				break
	if flag:
		print (-1)
		continue

	a -= s.count("0")
	b -= s.count("1")
	# print (a, b, s)

	for i in range(n//2):
		if s[i]=="?":
			if a>1:
				s[i] = s[n-i-1] = "0"
				a -= 2
			else:
				s[i] = s[n-i-1] = "1"
				b -= 2

	if n%2:
		if s[n//2]=="?":
			if a:
				s[n//2] = "0"
				a -= 1
			else:
				s[n//2] = "1"
				b -= 1

	# print (a, b, s)


	if a==0 and b==0 and s.count("?")==0:
		print ("".join(s))
	else:
		print (-1)
