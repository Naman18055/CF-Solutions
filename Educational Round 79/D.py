from fractions import Fraction
import sys
input = sys.stdin.readline
def modInverse(a, m) : 
	m0 = m 
	y = 0
	x = 1
  
	if (m == 1) : 
		return 0
  
	while (a > 1) : 
  
		# q is quotient 
		q = a // m 
  
		t = m 
  
		# m is remainder now, process 
		# same as Euclid's algo 
		m = a % m 
		a = t 
		t = y 
  
		# Update x and y 
		y = x - q * y 
		x = t 
  
  
	# Make x positive 
	if (x < 0) : 
		x = x + m0 
  
	return x


n=int(input())
l=[]
for i in range(n):
	l.append(list(map(int,input().split()))[1:])
count={}
for i in l:
	for j in i:
		if str(j) in count:
			count[str(j)]+=1
		else:
			count[str(j)]=1
ans=Fraction(0,1)
final=0
for i in range(n):
	for j in l[i]:
		ans=(Fraction(count[str(j)],n)*Fraction(1,len(l[i])))
		final+=(((ans.numerator)*modInverse(ans.denominator*n,998244353))%998244353)
	final=final%998244353
print (final)

