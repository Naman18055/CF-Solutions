import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	o = 0
	for i in a:
		if i%2:
			o += 1
	if o==n:
		print ("Yes")
	else:
		print ("No")