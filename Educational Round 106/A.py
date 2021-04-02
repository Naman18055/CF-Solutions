for nt in range(int(input())):
	n, k1, k2 = map(int,input().split())
	w, b = map(int,input().split())
	f = False
	if (k1+k2)//2>=w:
		f = True
	if not f:
		print ("NO")
		continue
	f = False
	if (n-k1+n-k2)//2>=b:
		f = True
	if not f:
		print ("NO")
		continue
	print ("YES")