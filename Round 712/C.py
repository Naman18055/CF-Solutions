for nt in range(int(input())):
	n = int(input())
	s = input()
	a = []
	b = []
	ans1, ans2 = "", ""
	if s[0]=="0" or s[-1]=="0":
		print ("NO")
		continue
	c = s.count("1")
	d = 0
	ans = "YES"

	if True:
		prev = 1
		for i in range(n):
			if s[i]=="0":
				if prev:
					a.append("(")
					if not b:
						ans = "NO"
						break
					b.pop()
					ans1 += a[-1]
					ans2 += ")"
				else:
					b.append("(")
					if not a:
						ans = "NO"
						break
					a.pop()
					ans2 += b[-1]
					ans1 += ")"
				prev = 1-prev
			else:
				d += 1
				if d>c//2 and a and b:
					a.pop()
					b.pop()
					ans1 += ")"
					ans2 += ")"
				else:
					ans1 += "("
					ans2 += "("
					a.append("(")
					b.append("(")
		if a or b:
			print ("NO")
			continue
		print (ans)
		print (ans1)
		print (ans2)

	else:
		pass



			

