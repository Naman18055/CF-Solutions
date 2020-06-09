for nt in range(int(input())):
	a,b,c,n=list(map(int,input().split()))
	if (a+b+c+n)%3!=0:
		print ("NO")
		continue
	v = (a+b+c+n)//3
	if a>v or b>v or c>v:
		print ("NO")
		continue
	print ("YES")