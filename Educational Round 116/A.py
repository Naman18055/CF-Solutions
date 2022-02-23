for nt in range(int(input())):
	s = input()
	if s[0]==s[-1]:
		print (s)
	elif s[0]=="a":
		print ("b"+s[1:])
	else:
		print ("a"+s[1:])