import math
n = int(input())
prod = 1
ans = []
for i in range(1, n):
	if math.gcd(n, i)==1:
		ans.append(i)
		prod = (prod*i)%n
if prod!=1:
	ans.remove(prod)
print (len(ans))
print (*ans)

