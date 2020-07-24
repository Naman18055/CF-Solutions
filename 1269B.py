from collections import Counter

def check(num):
	new = []
	for i in a:
		new.append((i+num)%m)
	new.sort()
	if new==b:
		return True
	return False

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()
c1 = Counter(a)
c2 = Counter(b)
d = {}
for i in c2:
	if c2[i] not in d:
		d[c2[i]] = [i]
	else:
		d[c2[i]].append(i)
# print (d)

ans = m
num = a[0]
for i in d[c1[num]]:
	x = (i-num)%m
	if check(x):
		ans = min(ans,x)
print (ans)