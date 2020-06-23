def calc(s):
	b = bin(s)[2:]
	b = "0"*(x-len(b))+b
	c = ""
	for i in b:
		if i=="1":
			c += "0"
		else:
			c += "1"
	return int(c,2)

n = int(input())
a = list(map(int,input().split()))
x = len(bin(max(a))[2:])
if n==1:
	print (a[0])
	exit()
p = [calc(a[0])]
s = [0]*n
s[-1] = calc(a[-1])
for i in range(1,n):
	p.append(p[-1]&calc(a[i]))
for i in range(n-2,-1,-1):
	s[i] = (s[i+1]&calc(a[i]))
maxx = a[0]&s[1]
ind = 0
# print (p,s)
for i in range(1,n-1):
	if (p[i-1]&a[i]&s[i+1])>maxx:
		maxx = (p[i-1]&a[i]&s[i+1])
		ind = i
if (p[-2]&a[-1])>maxx:
	maxx = p[-2]&a[-1]
	ind = n-1	
# print (maxx)
print (a[ind],*(a[0:ind]+a[ind+1:]))