for nt in range(int(input())):
	p, a, b, c = map(int,input().split())
	if p%a==0:
		print (0)
		continue
	if p%b==0:
		print (0)
		continue
	if p%c==0:
		print (0)
		continue
	print (min(a-p%a,b-p%b, c-p%c))