for nt in range(int(input())):
	n = int(input())
	s1 = input()
	s2 = input()
	prev = False
	ans = 0
	for i in range(n):
		if s1[i]=="0" and s2[i]=="0":
			if prev=="11":
				ans += 2
				prev = False
			elif prev=="00":
				ans += 1
			else:
				prev = "00"
		elif s1[i]+s2[i]=="01" or s1[i]+s2[i]=="10":
			if prev=="00":
				ans += 1
		
			ans += 2
			prev = False
		else:
			if prev=="00":
				ans += 2
				prev = False
			else:
				prev = "11"
	if prev=="00":
		ans += 1
	print (ans)