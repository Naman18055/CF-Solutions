for nt in range(int(input())):
	s="R"+input()+"R"
	gap=0
	prev="R"
	count = 0
	for i in range(1,len(s)):
		if s[i]=="L" and prev=="R":
			count=1
			prev="L"
		elif s[i]=="L":
			count+=1
		else:
			#print (count)
			if count>gap:
				gap=count
			count=0
	print (gap+1)