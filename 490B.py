n = int(input())
a,b = [],[]
for i in range(n):
	x,y = map(int,input().split())
	a.append(x)
	b.append(y)
s1 = set(a)
s2 = set(b)
ans = [-1]*n
for i in s1:
	if i not in s2:
		ans[0] = i
		break
for i in s2:
	if i not in s1:
		ans[-1] = i
		break
d = {}
for i in range(n):
	d[a[i]] = b[i]
ans[1] = d[0]
for i in range(2,n-1):
	ans[i] = d[ans[i-2]]
print (*ans)