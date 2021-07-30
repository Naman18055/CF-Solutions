for nt in range(int(input())):
	n, m, k = map(int,input().split())
	v = n*m//2 - k
	if m%2:
		v -= n//2
	elif n%2:
		k -= m//2
	if k%2==0 and v%2==0 and v>=0 and k>=0:
		print ("YES")
	else:
		print ("NO")