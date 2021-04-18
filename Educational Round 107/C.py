n, q = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
for i in range(n):
	if a[i] not in d:
		d[a[i]] = i+1

for i in b:
	print (d[i], end=" ")
	curr = d[i]
	for j in d:
		if d[j]<curr:
			d[j] += 1
	d[i] = 1
print ()