import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, d = map(int,input().split())
	a = sorted(list(map(int,input().split())))
	if max(a)<=d:
		print ("YES")
		continue
	if len(a)>1 and a[0]+a[1]<=d:
		print ("YES")
		continue
	print ("NO")