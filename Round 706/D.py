import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
l, c = [], 1
for i in range(1, n):
	if a[i]<a[i-1]:
		c += 1
	else:
		l.append(c)
		c = 1
l.append(c)
c = 1
for i in range(n-2, -1, -1):
	if a[i]<a[i+1]:
		c += 1
	else:
		l.append(c)
		c = 1
l.append(c)
l.sort()
if l.count(max(l))!=2:
	print (0)
	exit()

c = 1
start1=0
for i in range(1, n):
	if a[i]<a[i-1]:
		c += 1
	else:
		if c==l[-1]:
			break
		c = 1
		start1 = i
c = 1
start2=n-1
for i in range(n-2, -1, -1):
	if a[i]<a[i+1]:
		c += 1
	else:
		if c==l[-1]:
			break
		c = 1
		start2 = i
	# print (i, c, start2)
# print (l, start1, start2)

if a[0]==10**18:
	print (start1, start2, l[::-1])
if start1==start2 and l[-1]%2:
	print (1)
else:
	print (0)

