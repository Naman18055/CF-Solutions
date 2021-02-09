for nt in range(int(input())):
	n = int(input())
	s = input()
	o,z = 0, 0
	for i in range(n-1):
		if s[i]=="0" and s[i+1]=="0":
			z += 1
		if s[i]=="1" and s[i+1]=="1":
			o += 1
	print (max(o, z))
