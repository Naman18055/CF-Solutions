import math

def eculidean_algo(a,b):
	g = math.gcd(a,b)
	x,y = a,b
	while x%y!=g:
		x,y = y,x%y

a,b,c = map(int,input().split())
g = math.gcd(a,b)
if c%g!=0:
	print (-1)
	exit()
euclidean_algo(a,b)