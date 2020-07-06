n = int(input())
a = list(map(int,input().split()))
d = {}
i = 0
while i<n:
	num = a[i]
	while num in d:
		a[d[num]] = -1
		del d[num]
		num = num*2
	d[num] = i
	a[i] = num
	i += 1
ans = []
for i in a:
	if i!=-1:
		ans.append(i)
print (len(ans))
print (*ans)
