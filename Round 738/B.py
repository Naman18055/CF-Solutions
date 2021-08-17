for nt in range(int(input())):
	n = int(input())
	a = list(input())
	if a.count("?")==n:
		print ("RB"*(n//2)+"R"*(n%2))
		continue

	for i in range(1, n):
		if a[i]=="?" and a[i-1]!="?":
			if a[i-1]=="R":
				a[i]="B"
			else:
				a[i]="R"
	for i in range(n-2, -1, -1):
		if a[i]=="?":
			if a[i+1]=="R":
				a[i] = "B"
			else:
				a[i] = "R"
	print ("".join(a))


	