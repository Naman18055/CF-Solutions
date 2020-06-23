n = int(input())
a = list(map(int,input().split()))
a.sort()
d = {}
ans = 0
i = 0
while len(d)!=n:
	if a[i] not in d:
		d[a[i]] = 1
		i += 1
	else:
		while a[i] in d:
			ans += 1
			a[i] += 1
		d[a[i]] = 1
		i += 1
print (ans)