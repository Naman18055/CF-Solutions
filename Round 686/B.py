from collections import Counter
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	minn = 10**18
	for i in c:
		if c[i]==1:
			minn = min(minn, i)
	if minn==10**18:
		print (-1)
	else:
		print (a.index(minn)+1)