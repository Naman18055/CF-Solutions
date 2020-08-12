n,d,m = map(int,input().split())
a = list(map(int,input().split()))
b,c = [],[]
for i in range(n):
	if a[i]<=m:
		b.append(a[i])
	else:
		c.append(a[i])
c.sort(reverse=True)
b.sort()
if len(b)==0:
	j = len(c)-1
	ans = 0
	for i in range(n):
		if i>j:
			break
		ans += c[i]
		j -= d
	print (ans)
	exit()

pref = [b[0]]
for i in range(1,len(b)):
	pref.append(pref[-1]+b[i])
ans = 0
maxx = sum(b)
for i in range(len(c)):
	ans += c[i]
	skip = i*d
	left = max(0,skip-(len(c)-i-1))
	if left>len(pref):
		break
	if not left:
		maxx = max(maxx,ans+pref[-1])
	else:
		maxx = max(maxx,ans + pref[-1] - pref[left-1])

print (maxx)