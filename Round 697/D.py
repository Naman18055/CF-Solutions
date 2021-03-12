import sys
input = sys.stdin.readline

def calc(s, arr):
	left = m - s
	low = 0
	high = len(arr)-1
	if arr[-1]<left:
		return -1
	while low<high:
		mid = (low+high)//2
		if arr[mid]>=left:
			high = mid-1
		else:
			low = mid+1
	if arr[low]>=left:
		return low + 1
	else:
		return low + 2

for nt in range(int(input())):
	n, m = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	if sum(a)<m:
		print (-1)
		continue

	d = {1: [], 2:[]}
	for i in range(n):
		d[b[i]].append(a[i])
	d[1] = sorted(d[1])[::-1]
	d[2] = sorted(d[2])[::-1]
	if len(d[1])==0:
		p = [d[2][0]]
		for i in range(1, len(d[2])):
			p.append(p[-1]+d[2][i])
		ans = calc(0, p)
		print (2*ans)
		continue
	if len(d[2])==0:
		p = [d[1][0]]
		for i in range(1, len(d[1])):
			p.append(p[-1]+d[1][i])
		ans = calc(0, p)
		print (ans)
		continue

	p = [d[2][0]]
	for i in range(1, len(d[2])):
		p.append(p[-1]+d[2][i])

	ans = sum(b)
	s1 = 0
	for i in range(len(d[1])):
		if s1>=m:
			if i<ans:
				ans = i
			break
		f = calc(s1, p)
		# print (s1, f)
		s1 += d[1][i]
		if f == -1:
			continue
		if i + 2*(f)<ans:
			ans = i+2*f
	if s1>=m:
		if i+1<ans:
			ans = i+1
	f = calc(s1, p)
	if i+1+2*f<ans:
		ans = i+1+2*f
	print (ans)


