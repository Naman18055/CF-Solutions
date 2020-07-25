n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if max(a)>min(b):
	print (-1)
	exit()
a.sort(reverse=True)
b.sort()
j = m-1
i = 0
ans = 0
while j>=0:
	if j==0:
		if b[j]==a[i]:
			ans += b[j]
			flag = 1
			break
		else:
			ans += a[i]
			flag = 0
			break
	if b[j]>=a[i]:
		ans += b[j]
		j -= 1

# print (ans)
for i in range(1,n):
	ans += a[i]*m
# print (ans)
if flag:
	print (ans)
else:
	print (ans + b[0]-a[1])