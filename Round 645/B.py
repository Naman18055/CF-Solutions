import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	sub = 0
	for i in range(n-1,-1,-1):
		if l[i]>i+1:
			sub+=1
		else:
			break
	print (n-sub+1)