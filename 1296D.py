n,a,b,k = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(n):
	arr[i] = arr[i]%(a+b)
	if arr[i]==0:
		arr[i] += (a+b)
	arr[i] = (arr[i]-1)//a
ans = 0
arr.sort()
for i in range(n):
	if arr[i]>k:
		break
	k -= arr[i]
	ans += 1
print (ans)