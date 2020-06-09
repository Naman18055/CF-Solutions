n=int(input())
s=input()
c=s.count("8")
a=(n-11)//2
if a>=c:
	print ('NO')
else:
	count=0
	s1=""
	for i in range(n):
		#print (i,count,a)
		if count==a:
			s1+=s[i:]
			break
		else:
			if s[i]!="8":
				s1+=s[i]
			else:
				count+=1
	#print (s1)
	if "8" in s1[0:a+1]:
		print ('YES')
	else:
		print ('NO')