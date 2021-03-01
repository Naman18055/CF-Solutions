
for nt in range(int(input())):
	n = int(input())
	r = list(map(int,list(input())))
	b = list(map(int,list(input())))
	ar = 0
	br = 0
	# print (r)
	# print (b)
	for i in range(n):

		if r[i]>b[i]:
			ar += 1
		elif b[i]>r[i]:
			br += 1

	if ar>br:
		print ("RED")
	elif br>ar:
		print ("BLUE")
	else:
		print ("EQUAL")