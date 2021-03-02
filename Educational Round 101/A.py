for nt in range(int(input())):
	s = input()
	n = len(s)
	if n%2 or s[0]==")" or s[-1]=="(":
		print ("NO")
		continue

	if s.count(")")>n//2 or s.count("(")>n//2:
		print ("NO")
	else:
		print ("YES")

