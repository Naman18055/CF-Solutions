n = int(input())
s = input()
m = int(input())
names = []
for i in range(m):
	names.append(input())
loc = {}
for i in range(n):
	if s[i] not in loc:
		loc[s[i]] = [i]
	else:
		loc[s[i]].append(i)
for i in names:
	done = {}
	ans = 0
	for j in i:
		if j in done:
			ans = max(ans,loc[j][done[j]])
			done[j] += 1
		else:
			ans = max(ans,loc[j][0])
			done[j] = 1
	print (ans+1)