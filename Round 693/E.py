import sys
input = sys.stdin.readline

def find_num(t, arr, num, find_index):
	low = 0
	high = len(arr)-1
	while low<high:
		mid = (low+high)//2
		if arr[mid][0]>=t[0]:
			high = mid - 1
		else:
			low = mid + 1
	# print (low)
	if arr[low][0]>=t[0]:
		if low>0 and num[low-1][0]<t[1]:
			return find_index[tuple(arr[num[low-1][1]])]
		return -1
	else:
		if num[low][0]<t[1]:
			return find_index[tuple(arr[num[low][1]])]
		return -1

for nt in range(int(input())):
	n = int(input())
	a = []
	d1, d2 = {}, {}
	c1, c2 = [], []
	for i in range(n):
		a.append(list(map(int,input().split())))
		d1[tuple(a[-1])] = i+1

	b = sorted(a)
	c1.append([b[0][1], 0])
	for i in range(1, n):
		if b[i][1]<c1[-1][0]:
			c1.append([b[i][1], i])
		else:
			c1.append([c1[-1][0], c1[-1][1]])

	c = []
	for i in range(n):
		c.append([a[i][1], a[i][0]])
		d2[tuple(c[-1])] = i+1
	c.sort()
	c2.append([c[0][1], 0])
	for i in range(1, n):
		if c[i][1]<c2[-1][0]:
			c2.append([c[i][1], i])
		else:
			c2.append([c2[-1][0], c2[-1][1]])


	ans = []
	for i in a:
		# print (i, b, c1, d1)
		x = find_num(i, b, c1, d1)
		if x==-1:
			y = find_num(i, c, c2, d2)
			ans.append(y)
		else:
			ans.append(x)

	print (*ans)