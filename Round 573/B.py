a,b,c = input().split()
if (a==b and b==c):
	print (0)
	exit()
x = sorted([int(a[0]),int(b[0]),int(c[0])])
if (a[1]==b[1] and b[1]==c[1]) and (x[0]+1==x[1] and x[1]+1==x[2]):
	print (0)
	exit()
if a==b or b==c or a==c:
	print (1)
	exit()
d = {"p":[],"m":[],"s":[]}
d[a[1]].append(a)
d[b[1]].append(b)
d[c[1]].append(c)
ans = 2
flag = 0
for i in d:
	if len(d[i])==2:
		x = sorted([int(d[i][0][0]),int(d[i][1][0])])
		if x[1]-x[0]<=2:
			ans = min(ans,1)
	elif len(d[i])==3:
		x = sorted([int(d[i][0][0]),int(d[i][1][0]),int(d[i][2][0])])
		if x[1]-x[0]<=2 or x[2]-x[1]<=2:
			ans = min(ans,1)
print (ans)
