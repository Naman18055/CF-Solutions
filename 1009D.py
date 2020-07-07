from math import gcd
n,m = map(int,input().split())
if m<n-1:
	print ("Impossible")
	exit()
	
ans = []
for i in range(1,n+1):
	for j in range(i+1,n+1):
		if gcd(i,j)==1:
			m -= 1
			ans.append((i,j))
		if m==0:
			break
	if m==0:
		break
if m!=0:
	print ("Impossible")
else:
	print ("Possible")
	for i in ans:
		print (i[0],i[1])