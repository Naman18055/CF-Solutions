def check(num):
	cost = []
	for i in range(n):
		cost.append(a[i]+((i+1)*num))
	cost.sort()
	if sum(cost[0:num])<=s:
		return True,sum(cost[0:num])
	return False,-1


n,s = map(int,input().split())
a = list(map(int,input().split()))
low = 0
high = n
while low<high:
	mid = (low+high)//2
	if check(mid)[0]:
		low = mid+1
	else:
		high = mid-1
if check(low)[0]:
	print (low,check(low)[1])
else:
	print (low-1,check(low-1)[1])