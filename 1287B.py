def calc(a,b):
	ans = ""
	for i in range(k):
		if a[i]==b[i]:
			ans += a[i]
		else:
			if a[i]!="T" and b[i]!="T":
				ans += "T"
			elif a[i]!="S" and b[i]!="S":
				ans += "S"
			else:
				ans += "E"
	return ans

n,k = map(int,input().split())
d = {}
a = []
for i in range(n):
	s = input()
	a.append(s)
	d[s] = 1
count = 0
for i in range(n):
	for j in range(i+1,n):
		if calc(a[i],a[j]) in d:
			count += 1
print (count//3)