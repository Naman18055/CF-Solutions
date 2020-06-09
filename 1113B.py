def primes(n):
	for i in range(2,int(n**(1/2))+1):
		if n%i==0:
			return False
	return True

def factors(n):
	temp=[]
	for i in range(2,n):
		if n%i==0:
			temp.append(i)
	return temp

n=int(input())
l=list(map(int,input().split()))
l.sort()
m=sum(l)
small=m
for i in range(n-1,-1,-1):
	if not primes(l[i]):
		f=factors(l[i])
		for j in f:
			if (m-(l[i])*(j-1)//j+(l[0])*(j-1))<small:
				small=(m-(l[i])*(j-1)//j+(l[0])*(j-1))
print (small)