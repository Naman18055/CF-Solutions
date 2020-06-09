def check(num):
	if values[num-1]>n:
		return False
	return values[num-1]

s=""
for i in range(1,100000):
	s+=str(i)
values=[1]
prev=1
for i in range(2,30000):
	values.append(values[-1]+prev+len(str(i)))
	prev=prev+len(str(i))
# print (values)
for nt in range(int(input())):
	n=int(input())
	low=0
	high=3*(10**4)
	while low<high:
		mid=(low+high)//2
		if check(mid):
			low=mid+1
		else:
			high=mid-1
	if check(low):
		ans=low
	else:
		ans=low-1
	value = check(ans)
	left = n-value
	# print (ans,value,left)
	if left==0:
		print (str(ans)[-1])
	else:
		print (s[left-1])