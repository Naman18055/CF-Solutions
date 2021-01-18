for nt in range(int(input())):
	n = input()
	ans = (int(n[0])-1)*10
	if len(n)==1:
		ans += 1
	elif len(n)==2:
		ans += 3
	elif len(n)==3:
		ans += 6
	else:
		ans += 10
	print (ans)
