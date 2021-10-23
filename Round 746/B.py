import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, x = map(int,input().split())
	a = list(map(int,input().split()))
	b = sorted(a)
	if b==a:
		print ("YES")
		continue

	if x==n:
		print ("NO")
		continue

	if x<=n//2:
		print ("YES")
		continue

	if b[n-x:x]==a[n-x:x]:
		print ("YES")
	else:
		print ("NO")
	