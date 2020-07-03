import math
c,d = map(int,input().split())
n,m = map(int,input().split())
k = int(input())
if k>=n*m:
	print (0)
	exit()
left = n*m-k
print (min(math.ceil(left/n)*c,(left//n)*c + (left%n)*d,left*d))