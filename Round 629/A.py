
for nt in range(int(input())):
	a,b=map(int,input().split())
	if a%b==0:
		print (0)
		continue
	print (b-a%b)