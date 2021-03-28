n, m = map(int,input().split())
a = input()
b = input()
s = []
c = n-1
for i in range(m-1, -1, -1):
	for j in range(c, -1, -1):
		if a[j]==b[i]:
			s.append(j)
			c = j-1
			break
s = s[::-1]
# print (s)

maxx = 0
c = 0
for i in range(m-1):
	for j in range(c, n):
		if a[j]==b[i]:
			c = j+1
			maxx = max(maxx, s[i+1]-j)
			break
print (maxx)

