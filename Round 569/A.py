n=int(input())
l=[1]
x=4
for i in range(101):
	l.append(l[-1]+x)
	x+=4
print (l[n-1])