# import sys
# input = sys.stdin.readline


def bs(num):
	low = 0
	high = len(a)-1
	while low<high:
		mid = (low+high)//2
		if a[mid]<num:
			low = mid + 1
		else:
			high = mid - 1
	if a[low]<num:
		return low + 1
	else:
		return low

n = int(raw_input())
a = sorted(list(map(int,raw_input().split())))
s = sum(a)
m = int(raw_input())
b = []
for i in range(m):
	b.append(list(map(int,raw_input().split())))

for i in b:
	if a[-1]<i[0]:
		print (i[0]-a[-1]+max(0, i[1]-(s-a[-1])))
		continue
	if a[0]>i[0]:
		print (max(0, i[1]-(s-a[0])))
		continue

	ind = bs(i[0])
	print (max(0, min(max(0, i[1]-(s-a[ind])), i[0]-a[ind-1]+max(0, i[1]-(s-a[ind-1])))))