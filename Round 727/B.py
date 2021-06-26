n, q = map(int,input().split())
s = input()
a = [0]
for i in range(n):
	a.append(a[-1]+ord(s[i])-96)
for i in range(q):
	l, r = map(int,input().split())
	print (a[r]-a[l-1])
