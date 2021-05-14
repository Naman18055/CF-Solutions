import sys
from collections import Counter
input = sys.stdin.readline

def maxx(num):
	low = 0
	high = len(arr)-1
	while low<high:
		mid = (low+high)//2
		if arr[mid][0]>=num:
			high = mid - 1
		else:
			low = mid + 1
	if arr[low][0]>num:
		return low - 1
	else:
		return low

for nt in range(int(input())):
	n, w = map(int,input().split())
	a = list(map(int,input().split()))
	c = Counter(a)
	arr = []
	for i in c:
		arr.append([i, c[i]])
	arr.sort()

	k = w
	ans = 1
	while arr:
		if k<arr[0][0]:
			ans += 1
			k = w
		m = maxx(k)
		# print (k, arr, m)
		k -= arr[m][0]
		arr[m][1] -= 1
		if arr[m][1]==0:
			arr.pop(m)
	print (ans)


