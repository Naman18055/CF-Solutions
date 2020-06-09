for nt in range(int(input())):
	s = input()
	o = [0,0]
	v = {(0,0):0}
	ans = 0
	for i in s:
		p = tuple(o)
		if i=="N":
			o[1]+=1
		elif i=="S":
			o[1]-=1
		elif i=="W":
			o[0]-=1
		else:
			o[0]+=1
		if p+tuple(o) in v or tuple(o)+p in v:
			ans += 1
		else:
			v[p+tuple(o)] = 0
			ans += 5
		# print (o)
	print (ans)