s=input()
a=s.count("o")
b=len(s)-a
if a==0:
	print ("YES")
	exit()
if b%a==0:
	print ("YES")
else:
	print ("NO")