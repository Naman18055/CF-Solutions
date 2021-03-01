import math

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if len(a)==1:
	print (*(b[i]+a[0] for i in range(m)))
	exit()

diff = []
for i in range(1, n):
	diff.append(a[i]-a[i-1])
hcf = diff[0]
for i in diff:
	hcf = math.gcd(hcf, i)
ans = []
for i in b:
	ans.append(math.gcd(a[0]+i, hcf))
print (*ans)