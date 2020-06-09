import math

def check2(case):
	for i in case:
		for j in range(len(i)):
			if len(i)-j>c[i[j]-1]:
				return False
	return True

def check(test):
	if math.ceil(n//test)>c[0]:
		return [False]
	cases=[[] for i in range(test)]
	for i in range(n):
		cases[i%test].append(m[i])
	if check2(cases):
		return [True,cases]
	else:
		return [False]

n,k=map(int,input().split())
m=sorted(list(map(int,input().split())))
c=list(map(int,input().split()))
low=1
high=n+1
while low<high:
	# print (low,high)
	mid=(low+high)//2
	if check(mid)[0]:
		high=mid-1
	else:
		low=mid+1
# print (low,high)
if check(low)[0]:
	ans=low
else:
	ans=low+1
# print (check(ans))
arr=check(ans)[1]
print (ans)
for i in arr:
	print (len(i),end=" ")
	print (*i)
