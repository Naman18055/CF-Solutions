import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	curr = 0
	ans = "NO"
	for i in range(1,n):
		if a[i]<a[i-1] and not curr:
			continue
		elif a[i]<a[i-1] and curr:
			ans = "YES"
			break
		elif a[i]>a[i-1] and not curr:
			curr = 1
	print (ans)
	if ans == "YES":
		for i in range(1,n-1):
			if a[i]>a[i-1] and a[i]>a[i+1]:
				print (i,i+1,i+2)
				break
		