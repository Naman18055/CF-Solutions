def primefactors(n):
	primes=[]
	if n%2==0:
		primes.append(2)
		while n%2==0:
			n=n//2
	for i in range(3,int(n**(0.5))+1,2):
		if n%i==0:
			primes.append(i)
			while n%i==0:
				n=n//i
	if n!=1:
		primes.append(n)
	return primes

# def power(x, y): 
  
# 	if(y == 0): 
# 		return 1
# 	temp = power(x, int(y / 2))  
	  
# 	if (y % 2 == 0): 
# 		return (temp * temp)%1000000007
# 	else: 
# 		if(y > 0): 
# 			return (x * temp * temp )%1000000007

x,n=map(int,input().split())
primes = primefactors(x)
ans=1
#print (primes)
for i in primes:
	divide=i
	while divide<=n:
		ans=(ans*(pow(i,(n//divide),1000000007)))%1000000007
		divide=divide*i
	#print (ans)
print ((ans)%1000000007)