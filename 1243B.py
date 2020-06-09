for nt in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	d = 0
	ind = []
	for i in range(n):
		if a[i]!=b[i]:
			d += 1
			ind.append(i)
	if d!=2:
		print ("NO")
		continue
	if a[ind[0]]==a[ind[1]] and b[ind[1]]==b[ind[0]]:
		print ("YES")
	else:
		print ("NO")