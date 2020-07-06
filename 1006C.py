n = int(input())
d = list(map(int,input().split()))
p = [d[0]]
s = [0]*n
s[-1] = d[-1]
for i in range(1,n):
	p.append(p[-1]+d[i])
for i in range(n-2,-1,-1):
	s[i] = s[i+1] + d[i]
s2 = {}
for i in range(n):
	s2[s[i]] = i
ans = 0
for i in range(n):
	if p[i] in s2 and s2[p[i]]>i:
		ans = max(ans,p[i])
print (ans)