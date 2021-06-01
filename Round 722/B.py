import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	last = 10**20
	while len(a)>0 and a[-1]>0:
		last = a.pop()
	if not a:
		print (1)
		continue
	diff = 10**18
	for i in range(1, len(a)):
		diff = min(diff, a[i]-a[i-1])
	# print (a, last)
	if last>diff:
		print (len(a))
	else:
		print (len(a)+1)