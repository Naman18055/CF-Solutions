n = int(input())
if not n%2:
	print ((n//2+1)**2)
else:
	k = n//2
	print (2*(k+1)*(k+2))
	