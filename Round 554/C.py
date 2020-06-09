def gcd(a,b):
	if (b == 0):
		 return a
	return gcd(b, a%b)

def divisors(a):
	temp=[]
	for i in range(1,a+1):
		if a%i==0:
			temp.append(i)
	return temp

a,b=map(int,input().split())
if b%a==0:
	print (0)
else:
	m=a*b/(gcd(a,b))
	for i in (divisors(abs(b-a))):
		x=i-(a%i)
		# x=1
		# while True:
		# 	if gcd(a+x,b+x)==i:
		# 		break
		# 	else:
		# 		x+=1
		lcm=((a+x)*(b+x))/gcd(a+x,b+x)
		if lcm<m:
			m=lcm
			ans=x
	print (ans)
