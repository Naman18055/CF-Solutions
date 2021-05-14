import math
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ind = a.index(min(a))
	print (n-1)
	for i in range(ind-1, -1, -1):
		if a[i]>=a[i+1]:
			print (i+1, i+2, a[i+1]+1, a[i+1])
			a[i] = a[i+1] + 1
			# print (*a)
		else:
			for j in range(a[i+1], 10000000):
				if math.gcd(j, a[i])==1 and math.gcd(j, a[i+2])==1:
					a[i+1] = j
					break
			print (i+1, i+2, a[i], a[i+1])

	for i in range(ind+1, n):
		if a[i]>=a[i-1]:
			print (i, i+1, a[i-1], a[i-1]+1)
			a[i] = a[i-1] + 1
			# print (*a)
		else:
			for j in range(a[i-1], 10000000):
				if math.gcd(j, a[i])==1 and math.gcd(j, a[i-2])==1:
					a[i-1] = j
					break
			print (i, i+1, a[i-1], a[i])


