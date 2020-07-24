def check(k):
	if max(s[0:-1])<s[-1]:
		return True
	return False

def solve(ind,s):
	for i in range(m):
		v[i].append(v[i][ind]-v[i][-2])
	v.sort(key = lambda x:x[-1])
	count = 0
	for i in range(m):
		count += v[i][ind]
	x = []
	k = 0
	while count<s:
		s -= v[k][-3]
		count -= v[k][ind]
		x.append(v[k][-2]+1)
		k += 1
	for i in range(m):
		v[i].pop()
	return x


n,m = map(int,input().split())
v = []
s = 0
for i in range(m):
	v.append(list(map(int,input().split())))
	v[-1].append(i)
	s += v[-1][-2]

res = m
ans = [i for i in range(1,m+1)]
for i in range(n-1):
	x = solve(i,s)
	if len(x)<res:
		res = len(x)
		ans = x[::]

print (res)
print (*ans)