import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if sorted(a)==a:
		print (0)
		continue
	if a[0]==1 or a[-1]==n:
		print (1)
		continue
	if a[-1]==1 and a[0]==n:
		print (3)
		continue
	print (2)