for nt in range(int(input())):
	s = input()
	f = s.find("11")
	if f==-1:
		print ("YES")
		continue
	ind = -1
	for i in range(len(s)-2, -1, -1):
		if s[i:i+2]=="00":
			ind = i
			break
	if ind>f:
		print ("NO")
	else:
		print ("YES")