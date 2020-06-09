import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	m = int(input())
	b = list(map(int,input().split()))
	o1,e1,o2,e2=0,0,0,0
	for i in range(n):
		if a[i]%2:
			o1+=1
		else:
			e1+=1
	for i in range(m):
		if b[i]%2:
			o2+=1
		else:
			e2+=1
	print (o1*o2 + e1*e2)