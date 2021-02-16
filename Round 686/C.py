from collections import Counter
import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	new = [a[0]]
	for i in range(1, n):
		if a[i]==a[i-1]:
			continue
		new.append(a[i])
	c = Counter(new)
	minn = 10**18
	for i in c:
		if i==new[0] and i==new[-1]:
			minn = min(c[i]-1, minn)
		elif i==new[0] or i==new[-1]:
			minn = min(c[i], minn)
		else:
			minn = min(minn, c[i]+1)
	print (minn)