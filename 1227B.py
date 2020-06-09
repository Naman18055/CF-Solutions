import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = [a[0]]
	m = 1
	d = {a[0]:1}
	flag = 0
	for i in range(1,n):
		if a[i]!=a[i-1]:
			ans.append(a[i])
			d[a[i]] = 1
		else:
			while m in d:
				m += 1
			if m>=a[i]:
				flag = 1
				break
			ans.append(m)
			d[m] = 1
	if flag:
		print (-1)
		continue
	print (*ans)