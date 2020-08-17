import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
if a[-3]+a[-2]<=a[-1]:
	print ("NO")
else:
	print ("YES")
	print (*(a[-2:]+a[0:-2][::-1]))