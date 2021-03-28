import sys
input = sys.stdin.readline

def check(num):
	c = [0]*(n+1)
	b = [0]*n
	mini = 10**18
	maxi = -10**19
	v = 0
	for i in range(n):
		if(a[i] >= num):
			b[i] = 1
		else:
			b[i] -= 1
		
		v += b[i]
		c[i+1] = v
		
		if(i >= k-1):
			mini = min(mini, c[i-k+1])
			maxi = max(maxi, v - mini)
	if maxi>0:
		return True
	return False

n, k = map(int,input().split())
a = list(map(int,input().split()))
low = min(a)
high = max(a)

while low<high:
	mid = (low+high)//2
	if check(mid):
		low = mid + 1
	else:
		high = mid - 1
if check(low):
	print (low)
else:
	print (low-1)