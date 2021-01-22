import sys
input = sys.stdin.readline
from heapq import *

def check(ans):
	h, k = [], 0
	heapify(h)
	for i in range(2*n):
		if arr[i][0]=="+":
			heappush(h, ans[k])
			k += 1
		else:
			if arr[i][1] != heappop(h):
				return False
	return True


n = int(input())
count = 0
arr = []
minus = []
flag = 1
for i in range(2*n):
	arr.append(input().split())
	if arr[-1][0]=="+":
		count += 1
	else:
		if count==0:
			flag = 0
		arr[-1][1] = int(arr[-1][1])
		minus.append(int(arr[-1][1]))
		if n - minus[-1] + 1 < count:
			flag = 0
		count -= 1
if not flag:
	print ("NO")
	exit()

try:
	loc = []
	ans = []
	i = 0
	while i<2*n:
		if arr[i][0]=="+":
			ans.append(0)
			i += 1
		else:
			loc.append(len(ans)-1)
			while i<2*n and arr[i][0]=="-":
				if ans[loc[-1]]!=0:
					loc.pop()
				ans[loc[-1]] = arr[i][1]
				loc[-1] -= 1
				i += 1
			if ans[loc[-1]]!=0:
				loc.pop()

	if 0 in ans or not check(ans):
		print ("NO")
	else:
		print ("YES")
		print (*ans)
except:
	print ("NO")





