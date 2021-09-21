for nt in range(int(input())):
	n = int(input())
	s = input()
	if s.count("a")==0 or s.count("a")==n:
		print (-1, -1)
		continue
	for i in range(n):
		if s[i]=="a" and s[i+1]=="b":
			ind = i
			break
		elif s[i]=="b" and s[i+1]=="a":
			ind = i
			break
	print (ind+1, ind+2)