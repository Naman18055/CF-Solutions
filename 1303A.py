for nt in range(int(input())):
	s=input()
	start,end=-1,-1
	for i in range(len(s)):
		if s[i]=="1":
			start=i
			break
	for i in range(len(s)-1,-1,-1):
		if s[i]=="1":
			end=i
			break
	if start==-1 or end==-1:
		print (0)
		continue
	print ((s[start:end+1]).count("0"))