import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	c = list(map(int,input().split()))
	ans = []
	prev = -1
	for i in range(n-1):
		if a[i]!=prev:
			ans.append(a[i])
			prev = a[i]
		else:
			ans.append(b[i])
			prev = b[i]
	if a[-1]!=ans[-1] and a[-1]!=ans[0]:
		ans.append(a[-1])
	elif b[-1]!=ans[-1] and b[-1]!=ans[0]:
		ans.append(b[-1])
	else:
		ans.append(c[-1])
	print (*ans)
