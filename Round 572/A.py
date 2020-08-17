n = int(input())
s = input()
o = s.count("1")
z = n-o
if o!=z:
	print (1)
	print (s)
else:
	print (2)
	print (s[0:-1],s[-1])