import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = a.count(1)
	if c<=n//2:
		x = n-c
		count = 0
		print (x)
		for i in a:
			if i==1 and count<x:
				count += 1
				continue
			print (i,end = " ")
		print ()
	else:
		x = (c//2)*2
		count = 0
		print (x)
		for i in a:
			if i==1 and count<x:
				print (i,end=" ")
				count += 1
			if count==x:
				break
		print ()


	