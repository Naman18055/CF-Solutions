import sys
input = sys.stdin.readline
n,k,q = map(int,input().split())
start = {}
end = {}
for i in range(n):
	x,y = map(int,input().split())
	if x not in start:
		start[x] = 1
	else:
		start[x] += 1
	if y not in end:
		end[y] = 1
	else:
		end[y] += 1
c = [0]*(200002)
if 0 in start:
	c[0] += start[0]
if 0 in end:
	c[1] -= end[0]

for i in range(1,200001):
	c[i] += c[i-1]
	if i in start:
		c[i] += start[i]
	if i in end:
		c[i+1] -= end[i]

for i in range(200001):
	if c[i]>=k:
		c[i] = 1
	else:
		c[i] = 0
for i in range(1,200001):
	c[i] += c[i-1]


for i in range(q):
	a,b = map(int,input().split())
	if a==0:
		print (c[b])
	else:
		print (c[b]-c[a-1])