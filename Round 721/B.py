for nt in range(int(input())):
	n = int(input())
	s = input()
	if s[::-1]==s:
		if s.count('0')==0:
			print ("DRAW")
			continue
		
		if n%2 and s[n//2]=="0" and s.count("0")!=1:
			print ("ALICE")
		else:
			print ("BOB")
		continue

	s = list(s)
	diff = False
	flag = False
	for i in range(n):
		if s[i]!=s[n-i-1]:
			if diff:
				flag = True
				break
			diff = True
			s[i] = "1"
			s[n-i-1] = "1"

	if flag or s.count("0")==0:
		print ("ALICE")
		continue


	if n%2 and s[n//2]=="0" and s.count("0")==1:
		print ("DRAW")
	else:
		print ("ALICE")
