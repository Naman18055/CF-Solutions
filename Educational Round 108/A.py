for nt in range(int(input())):
	r, b, d = map(int,input().split())
	m = min(r, b)
	r -= m
	b -= m
	if d==0:
		if r+b>0:
			print ("NO")
			continue
		else:
			print ("YES")
			continue

	if ((r+b-1)//(d)+1)>m:
		print ("NO")
	else:
		print ("YES")