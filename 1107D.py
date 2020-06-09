import math
import sys
# input = sys.stdin.readline
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

n = int(input())
table = []
for i in range(n):
	table.append(bin((1 << n) | int(raw_input(), 16))[3:])

r,c = [],[]
count = 1
for i in range(1,n):
	if table[i]==table[i-1]:
		count += 1
	else:
		r.append(count)
		count = 1
r.append(count)
count = 1
for i in range(1,n):
	flag = 0
	for j in range(n):
		if table[j][i]!=table[j][i-1]:
			flag = 1
			break
	if not flag:
		count += 1
	else:
		c.append(count)
		count = 1
c.append(count)

ans = r[0]
for i in range(len(r)):
	ans = gcd(ans,r[i])
for i in range(len(c)):
	ans = gcd(ans,c[i])
print (ans)