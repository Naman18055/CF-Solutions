for nt in range(int(input())):
	n = int(input())
	if n==1:
		print (0)
		continue

	print (int("1"*(len(bin(n)[2:])-(bin(n)[2:]).index("1")-1), 2))
