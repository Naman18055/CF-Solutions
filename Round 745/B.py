import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n, m, k = map(int,input().split())
	if k<=1:
		print ("NO")
		continue

	if m<n-1:
		print ("NO")
		continue

	if m>(n*(n-1))//2:
		print ("NO")
		continue

	if n==1:
		print ("YES")
		continue

	if m==(n*(n-1))//2:
		if k>2:
			print ("YES")
		else:
			print ("NO")
		continue

	if k>3:
		print ("YES")
	else:
		print ("NO")


