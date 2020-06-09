for nt in range(int(input())):
	s=input()
	if len(set(s))==1:
		print (s)
		continue
	print ("10"*len(s))