import sys
input = sys.stdin.buffer.readline

def check(num):
	for i in range(n):
		if values[i]>=num:
			return True
	return False

def calc():
	curr = days[0]
	j = -1
	while curr<=x:
		curr += days[j]
		j -= 1
	left = curr - x
	left = (left*(left+1))//2
	a = pref[0] + (pref[-1]-pref[j])
	ans = (a - left)
	values[0] = ans
	j += 1
	for i in range(1,n):
		# j += 1
		curr += days[i]
		curr -= days[j]
		while curr>x:
			j += 1
			curr -= days[j]
		curr = max(curr, 0)
		curr += days[j]
		left = curr-x
		left = (left*(left+1))//2
		if j<0:
			a = pref[i] + (pref[-1]-pref[j-1])
		elif j==0:
			a = pref[i]
		else:
			a = pref[i] - pref[j-1]
		# print (i,j,left,curr,a)
		values[i] = a - left


n,x = map(int,input().split())
days = list(map(int,input().split()))
count = []
for i in days:
	count.append((i*(i+1))//2)

prefix = [days[0]]
pref = [count[0]]
for i in range(1,n):
	prefix.append(prefix[-1]+days[i])
	pref.append(pref[-1]+count[i])
# print (prefix)
# print (count)
# print (pref)
if x==sum(days):
	print (pref[-1])
	exit()
values = [0]*n
calc()
# print (values)

maxx = sum(count)
low = 0
high = 10**18
while low<high:
	mid = (low+high)//2
	if check(mid):
		low=mid+1
	else:
		high=mid-1
if check(low):
	print (low)
else:
	print (low-1)