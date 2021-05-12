for nt in range(int(input())):
	n = int(input())
	if n%2:
		print ("NO")
		continue

	# area = (x**2)*(n//2)
	if n**0.5 == int(n**0.5):
		print("YES")
	else:
		if n%2:
			print("NO")
		else:
			n = n//2
			if n**0.5 == int(n**0.5):
				print ("YES")
			else:
				print ("NO")