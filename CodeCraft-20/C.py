import math
import sys
input = sys.stdin.readline
n,m,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
new=[]
for i in range(n-1,-1,-1):
	new.append(a)
# for i in range(1,n):
# 	prefixa.append(math.gcd(prefixa[-1],a[i]))
# for i in range(1,m):
# 	prefixb.append(math.gcd(prefixb[-1],b[i]))
for i in range(min(n,m)):
	if b[i]%p!=0 and a[i]%p!=0:
		print (i)
		exit()

