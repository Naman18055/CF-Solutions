import math
def gcd(a,b):
	if (b == 0):
		 return a
	return gcd(b, a%b)

def best(p,k,n):
	lcm = a*b//(gcd(a,b))
	m=0
	for i in range(k//lcm):
		m+=((p[i]*(x+y))//100)
	for i in range(k//a-k//lcm):
		m+=((p[i+(k//lcm)]*x)//100)
	for i in range(k//b-k//lcm):
		m+=((p[i+(k//a)]*y)//100)
	return m

t=int(input())
for nt in range(t):
	n=int(input())
	p=list(map(int,input().split()))
	x,a=map(int,input().split())
	y,b=map(int,input().split())
	k=int(input())
	if x<y:
		x,y=y,x
		a,b=b,a
	p.sort(reverse = True)
	m=best(p,n,n)
	if m<k:
		print (-1)
	elif m==k:
		print (n)
	else:
		start = 0
		end = n+1
		while (end-start>1):
			mid = (start+end)//2
			m=best(p,mid,n)
			#print (m,mid,find)
			if m<k:
				start = mid
			else:
				end = mid
		print (end)
