import math

def euclidean_algo(a,b):
	if not a:
		return 0,1,b
	x,y,gcd = euclidean_algo(b%a,a)
	return y-(b//a)*x,x,gcd

a,b,c = map(int,input().split())
g = math.gcd(a,b)
if c%g!=0:
	print (-1)
	exit()
x,y,hcf = euclidean_algo(a,b)
print (x*(-c//g),y*(-c//g))