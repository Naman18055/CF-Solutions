def find(num):
	low = 0
	high = n-1
	while low<high:
		mid = (low+high)//2
		if p[mid]>=num:
			high = mid-1
		else:
			low = mid+1
	if p[low]<num:
		return low+1
	else:
		return low

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
p = [a[0]]
for i in range(1,n):
	p.append(p[-1]+a[i])
for i in range(m):
	print (find(b[i])+1)