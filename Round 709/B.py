import sys
input = sys.stdin.readline

def check(num):
	m = -1
	for i in range(1, n):
		if a[i]>=a[i-1]:
			if a[i]-a[i-1]!=num:
				return 0
		else:
			if m==-1:
				m = a[i-1]+num-a[i]
			else:
				if a[i-1]+num-a[i]!=m:
					return 0
	if max(a)>=m and m!=-1:
		return 0
	b = sorted(a)
	if b==a:
		return -1

	return m


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1 or n==2:
		print (0)
		continue
	inc = -1
	for i in range(1, n):
		if a[i]>=a[i-1]:
			inc = a[i]-a[i-1]
			break
	if inc==-1:

		if sorted(a)==a[::-1]:
			f = True
			s = a[1]-a[0]
			for i in range(1, n):
				if a[i]-a[i-1]!=s:
					f = False
					break
			if f:
				print (0)
			else:
				print (-1)
		else:
			print (-1)
		continue
	ans = check(inc)
	# print (inc)
	if ans==-1:
		print (0)
	elif ans==0:
		print (-1)
	else:
		print (ans, inc)
