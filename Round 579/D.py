s = input()
t = input()
n,m = len(s),len(t)
i,j = 0,0
first = []
last = []
while j<m:
	if s[i]==t[j]:
		first.append(i)
		i += 1
		j += 1
	else:
		i += 1
i,j = n-1,m-1
while j>=0:
	if s[i]==t[j]:
		last.append(i)
		j -= 1
	i -= 1
last = last[::-1]
ans = max(last[0],n-first[-1]-1)
for i in range(m-1):
	ans = max(ans,last[i+1]-first[i]-1)
# print (first)
# print (last)
print (ans)