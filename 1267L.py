n,m,k = map(int,input().split())
s = list(input())
s.sort()
ans = [["" for i in range(m)] for j in range(k)]
j = len(s)-1
for i in range(k):
	ans[i][0] = s[i]
i = k
for x in range(1,m):
	for y in range(k):
		if ans[y][x-1]==ans[-1][x-1]:
			ans[y][x] = s[i]
			i += 1
		else:
			ans[y][x] = s[j]
			j -= 1

for x in range(k,n):
	ans.append([])
	for y in range(m):
		ans[-1].append(s[i])
		i += 1
# print (ans)
for i in range(n):
	ans[i] = "".join(map(str,ans[i]))
ans.sort()
for i in ans:
	print (i)