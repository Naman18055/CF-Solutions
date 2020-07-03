n,m,k = map(int,input().split())
e = []
for i in range(m):
	e.append(tuple(map(int,input().split())))
if k>0:
	a = set(list(map(int,input().split())))
else:
	a = {}
ans = 10**18
for i in e:
	if i[0] in a and i[1] in a:
		continue
	if i[0] in a or i[1] in a:
		ans = min(ans, i[2])
if ans==10**18:
	print (-1)
	exit()
print (ans)