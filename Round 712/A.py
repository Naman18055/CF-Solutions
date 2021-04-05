for nt in range(int(input())):
	s = input()
	n = len(s)
	if s.count("a")==n:
		print ("NO")
		continue
	print ("YES")
	if "a"+s==("a"+s)[::-1]:
		print (s+"a")
	else:
		print ("a"+s)