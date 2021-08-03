for nt in range(int(input())):
	n = int(input())
	s = "abcdefghijklmnopqrstuvwxyz"
	ans = 0
	if n<=26:
		print (s[0:n])
		continue

	if n%2:
		print ("a"*(n//2-1)+"bc"+"a"*(n//2))
	else:
		print ("a"*(n//2-1)+"b"+"a"*(n//2))