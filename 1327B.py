import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		a.append(list(map(int,input().split()))[1:])
	d = {}
	l = {}
	for i in range(n):
		flag = 0
		for j in a[i]:
			if j not in d:
				d[j] = 1
				flag = 1
				break
		if not flag:
			l[i] = 1
		# print (l,d)
	if len(l)==0:
		print ("OPTIMAL")
		continue
	print ("IMPROVE")
	for i in l:
		ans = i
		break
	for i in range(1,n+1):
		if i not in d:
			print (ans+1,i)
			break