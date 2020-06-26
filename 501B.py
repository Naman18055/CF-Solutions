n = int(input())
a = []
for i in range(n):
	a.append(input().split())
d = {}
for i in a:
	if i[0] in d:
		d[i[1]] = d[i[0]]
		del d[i[0]]
	else:
		d[i[1]] = i[0]
print (len(d))
for i in d:
	print (d[i],i)