from collections import Counter
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l1,l2 = {},{}
for i in range(n):
	l1[a[i]] = i
	l2[b[i]] = i
v = []
for i in range(1,n+1):
	if l2[i]-l1[i]<0:
		v.append(l2[i]-l1[i]+n)
		continue
	v.append(l2[i]-l1[i])
c = Counter(v)
m = 0
for i in c:
	m = max(m,c[i])
print (m)