import sys
import math
input = sys.stdin.readline

powersOf2 = [1]
for i in range(60):
	powersOf2.append(powersOf2[-1]*2)
for nt in range(int(input())):
	n, k = map(int,input().split())
	for i in powersOf2:
		if i>k:
			maxx = i
			break
	if n<=maxx:
		for i in range(61):
			if powersOf2[i]>=n:
				res = i
				break
		print (res)
		continue
	res = powersOf2.index(maxx)
	n -= maxx
	res += (n-1)//k+1
	print (res)

