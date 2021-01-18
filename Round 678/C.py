mod = 10**9+7
n,x,pos = map(int,input().split())
low = 0
high = n
ans = 1
big = n-x
small = x-1
count = 0
while low<high:
	# print (ans, big, small, count)
	mid = (low+high)//2
	if mid>pos:
		ans = (ans*big)%mod
		big -= 1
		high = mid
		count += 1
	elif mid==pos:
		count += 1
		low = mid + 1
	else:
		count += 1
		ans = (ans*small)%mod
		small -= 1
		low = mid+1

add = 1
# print (ans, count, big, small)
for i in range(1, n-count+1):
	add = (add*i)%mod
print ((ans*add)%mod)

