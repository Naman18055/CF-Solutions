n,k = map(int,input().split())
s = input()
d = {}
count = {}
for i in range(n):
	if s[i] not in count:
		count[s[i]] = 1
	else:
		count[s[i]] += 1
c = 0
for i in range(n):
	if s[i] not in d:
		d[s[i]] = 1
		c += 1
	else:
		d[s[i]] += 1
	if c>k:
		print ("YES")
		exit()
	if d[s[i]]==count[s[i]]:
		del d[s[i]]
		c -= 1
print ("NO")