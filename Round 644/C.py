for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	o = []
	e = []
	for i in a:
		if i%2:
			o.append(i)
		else:
			e.append(i)
	if not len(o)%2:
		print ("YES")
		continue
	ans = "NO"
	for i in o:
		for j in e:
			if abs(i-j)==1:
				ans = "YES"
				break
	print (ans)