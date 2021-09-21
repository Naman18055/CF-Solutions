xor = [0]
for i in range(1, 300010):
	xor.append(xor[-1]^i)

for nt in range(int(input())):
	a, b = map(int,input().split())
	p = xor[a-1]
	if p==b:
		print (a)
		continue

	if p^b != a:
		print (a+1)
	else:
		print (a+2)