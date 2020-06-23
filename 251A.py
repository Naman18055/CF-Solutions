def bs(num):
	low = 0
	high = n-1
	while low<high:
		mid = (low+high)//2
		if a[mid]-num>d:
			high = mid-1
		else:
			low = mid+1
	if a[low]-num>d:
		return low-1
	else:
		return low

n,d = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(n):
	f = bs(a[i])
	f = f-i
	ans += max(0,(f*(f-1))//2)
print (ans)