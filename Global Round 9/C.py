import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if a[-1]==n:
		print ("YES")
		continue
	if a[-1]==1:
		print ("NO")
		continue
	if a[0]>a[-1]:
		print ("NO")
	else:
		print ("YES")
