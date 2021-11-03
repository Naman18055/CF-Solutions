for nt in range(int(input())):
	n = input()
	a1, a2 = 0, 0
	found = 0
	for i in range(len(n)-1, -1, -1):
		if (n[i]=="2" or n[i]=="7") and found:
			break
		if n[i]=="5" and not found:
			a1 -= 1
			found = 1
		a1 += 1
	found = 0
	for i in range(len(n)-1, -1, -1):
		if (n[i]=="5" or n[i]=="0") and found:
			break
		if n[i]=="0" and not found:
			a2 -= 1
			found = 1
		a2 += 1
	print (min(a1, a2))