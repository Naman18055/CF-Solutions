import sys
import math
input = sys.stdin.readline
n,m,q = map(int,input().split())
g = math.gcd(n,m)
f,s = n//g,m//g
for nt in range(q):
	sx,sy,ex,ey = map(int,input().split())
	if sx!=ex:
		if sx==1:
			print ("YES" if (sy-1)//f==(ey-1)//s else "NO")
		else:
			print ("YES" if (sy-1)//s==(ey-1)//f else "NO")
	else:
		if sx==1:
			print ("YES" if (sy-1)//f==(ey-1)//f else "NO")
		else:
			print ("YES" if (sy-1)//s==(ey-1)//s else "NO")
