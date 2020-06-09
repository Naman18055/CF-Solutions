t=input()
length=len(t)
count=0
for i in t:
	if i=="a":
		count+=1
slength=(length+count)/2
if int(slength)==slength:
	s=t[0:int(slength)]
	s1=""
	for i in s:
		if i!="a":
			s1+=i
	s2=t[int(slength):]
	if s1==s2:
		print (s)
	else:
		print (":(")
else:
	print (":(")