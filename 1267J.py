import sys
from collections import Counter
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	minn = n
	for i in c:
		minn = min(c[i],minn)
	ans = n
	for i in range(1,minn+2):
		flag = 0
		scr = 0
		for j in c:
			scr += (c[j]-1)//i + 1
			if c[j]<((c[j]-1)//i + 1)*(i-1):
				flag = 1
				break
		# print (i,scr,minn,flag)
		if not flag:
			ans = min(ans,scr)
	print (ans)