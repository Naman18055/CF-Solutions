import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	if a[0]<0:
		print ("NO")
	else:
		print ("YES")
		print (a[-1]+1)
		print (*[i for i in range(a[-1]+1)])
