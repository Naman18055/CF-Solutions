s = input()
n = len(s)
g = []
ind = -1
for i in range(n-1):
	if s[i]=="v" and s[i+1]=="v":
		ind = i
		break
if ind ==-1:
	print (0)
	exit()
count = 1
for i in range(ind+1,n):
	if s[i]==s[i-1]:
		count += 1
	else:
		if count==1 and s[i]=="o":
			count = g.pop()+1
			continue
		g.append(count)
		count = 1
g.append(count)
c = 0
for i in range(0,len(g),2):
	g[i] -= 1
	c += g[i]
suff = [c]
pref = [g[0]]
for i in range(1,len(g)):
	if i%2:
		suff.append(suff[-1]-g[i-1])
		pref.append(pref[-1])
	else:
		suff.append(suff[-1])
		pref.append(pref[-1]+g[i])
# print (g)
# print (suff)
# print (pref)
ans = 0
for i in range(1,len(g),2):
	ans += (g[i]*pref[i]*suff[i])
print (ans)