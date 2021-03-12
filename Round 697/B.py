for nt in range(int(input())):
	n = int(input())
	z = n//2020
	y = n%2020
	if y>z:
		print ("NO")
	else:
		print ("YES")