for nt in range(int(input())):
	s = input()
	c = 1
	ans = 1
	q = 0

	p = ""
	for i in range(1, len(s)):
		if s[i]=="1":
			if s[i-1]=="0":
				c += 1
				ans += c
			elif s[i-1]=="1":
				c = 1
				ans += c
			else:
				if p=="":
					c += 1
					ans += c
				elif p=="0":
					c += 1
					ans += c
				else:
					c = q+1
					ans += c
			q = 0


		elif s[i]=="0":
			if s[i-1]=="1":
				c += 1
				ans += c
			elif s[i-1]=="0":
				c = 1
				ans += c
			else:
				if p=="":
					c += 1
					ans += c
				elif p=="1":
					c += 1
					ans += c
				else:
					c = q+1
					ans += c
			q = 0

		else:
			q += 1
			if s[i-1]=="1":
				p = "0"
				c += 1
				ans += c
			elif s[i-1]=="0":
				p = "1"
				c += 1
				ans += c
			else:
				if p=="":
					c += 1
					ans += c
				elif p=="0":
					p = "1"
					c += 1
					ans += c
				else:
					p = "0"
					c += 1
					ans += c


		# print (ans, s[0:i])
	print (ans)


