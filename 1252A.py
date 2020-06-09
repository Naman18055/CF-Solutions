n = int(input())
a = list(map(int,input().split()))
ans = []
for i in a:
	ans.append((n+1)-i)
print (*ans)