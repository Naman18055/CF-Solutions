n,m = map(int,input().split())
a = {}
b = {}
both = {}
for i in range(n):
	a[input()] = 1
for i in range(m):
	s = input()
	if s in a:
		both[s] = 1
		del a[s]
	else:
		b[s] = 1
if len(both)==0:
	if len(a)<=len(b):
		print ("No")
	else:
		print ("Yes")
	exit()
x = len(a) + (len(both)-1)//2 + 1
y = len(b) + len(both)//2
# print (x,y,a,b,both)
if x<=y:
	print ("No")
else:
	print ("Yes")
