import math
n,k = map(int,input().split())
if n<=(2*k+1):
	print (1)
	print (math.ceil(n/2))
	exit()
x = (math.ceil(n/(2*k+1)))
ans = [k+1]
for i in range(1,x-1):
	ans.append(ans[-1]+(2*k+1))
# print (ans)
if n-ans[-1]-k<=k:
	shift = (k-(n-ans[-1]-k)+1)
	for i in range(len(ans)):
		ans[i] -= shift
	print (x)
	ans.append(n)
else:
	print (x)
	ans.append(ans[-1]+(2*k+1))
print (*ans)