import sys
input = sys.stdin.readline

def check(i):
	if i==0 or i==n-1:
		return False
	if a[i]>a[i-1] and a[i]>a[i+1]:
		return True
	if a[i]<a[i-1] and a[i]<a[i+1]:
		return True
	return False

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	hv = [0]
	for i in range(1, n-1):
		if a[i]>a[i-1] and a[i]>a[i+1]:
			ans += 1
			hv.append(1)
		elif a[i]<a[i-1] and a[i]<a[i+1]:
			ans += 1
			hv.append(1)
		else:
			hv.append(0)
	hv.append(0)

	s = ans
	# print (hv, s)
	for i in range(1, n-1):
		if not hv[i]:
			continue
		ini = a[i]
		x = [hv[i-1], hv[i], hv[i+1]].count(1)

		a[i] = a[i+1]
		c = 0
		if check(i-1):
			c += 1
		if check(i):
			c += 1
		if check(i+1):
			c += 1
		# print (i, c, a)
		ans = min(ans, s-x+c)
		a[i] = ini

		a[i] = a[i-1]
		c = 0
		if check(i-1):
			c += 1
		if check(i):
			c += 1
		if check(i+1):
			c += 1
		ans = min(ans, s-x+c)
		a[i] = ini

	print (ans)




