def factors(n):
	l=[]
	for i in range(1,int(n**(1/2))+1):
		if n%i==0:
			l.append(i)
			l.append(n//i)
	return l

n=int(input())
f=factors(n)
if f[-1]>=5 and f[-2]>=5:
	s=""
	j=0
	while j<f[-2]:
		temp=['a',"e","i","o","u"]
		for i in range(f[-1]):
			s+=temp[(i%5)]
		j+=1
		if j==f[-2]:
			break
		temp=["e","i","o","u","a"]
		for i in range(f[-1]):
			s+=temp[(i%5)]
		j+=1
		if j==f[-2]:
			break
		temp=["i","o","u","a","e"]
		for i in range(f[-1]):
			s+=temp[(i%5)]
		j+=1
		if j==f[-2]:
			break
		temp=["o","u",'a',"e","i"]
		for i in range(f[-1]):
			s+=temp[(i%5)]
		j+=1
		if j==f[-2]:
			break
		temp=["u",'a',"e","i","o"]
		for i in range(f[-1]):
			s+=temp[(i%5)]
		j+=1
	print (s)
else:
	print (-1)
