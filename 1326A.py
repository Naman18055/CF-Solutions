for nt in range(int(input())):
	n=int(input())
	if n==1:
		print (-1)
		continue
	ans="3"
	s=3
	for i in range(n-2):
		ans+="2"
		s+=2
	if (s+2)%3==0:
		ans+="4"
	else:
		ans+="2"
	print (ans[::-1])