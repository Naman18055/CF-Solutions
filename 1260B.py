for nt in range(int(input())):
	a,b = map(int,input().split())
	if (a+b)%3!=0 or min(a,b)*2<max(a,b):
		print ("NO")
		continue
	print ("YES")