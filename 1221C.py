def check(num):
	if c<num or m<num:
		return False
	if c-num+m-num+x>=num:
		return True
	return False

for nt in range(int(input())):
	c,m,x=map(int,input().split())
	low=0
	high=10**9
	while low<high:
		mid=(low+high)//2
		if check(mid):
			low=mid+1
		else:
			high=mid-1
	if check(low):
		print (low)
	else:
		print (low-1)