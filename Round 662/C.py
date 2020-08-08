import sys
from collections import Counter
input = sys.stdin.readline

def check(num):
	new = 0
	temp = []
	for i in arr:
		temp.append(i[0])

	prev = 0
	k = ones
	while True:
		count = 0
		for i in range(len(arr)):
			if count<=num and temp[i]>0:
				new += 1
				count += 1
				temp[i] -= 1
			else:
				break

		temp.sort(reverse=True)

		if new != n: 
			if count<=num:
				k -= (num-count+1)
			if k<0:
				return False
			new += (num-count+1)
				
		# print (num,new,temp,count,k)
		if temp[0]<=1:
			return True




for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	arr = []
	ones = 0
	for i in c:
		if c[i]==1:
			ones += 1
			continue
		arr.append((c[i],i))
	arr.sort(reverse=True)

	low = 0
	high = n
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