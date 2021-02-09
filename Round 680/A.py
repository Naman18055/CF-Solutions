t = int(input())
for nt in range(t):
	n,x = map(int,input().split())
	a = sorted(list(map(int,input().split())))
	b = sorted(list(map(int,input().split())))[::-1]
	ans = "Yes"
	for i in range(n):
		if a[i]+b[i]>x:
			ans = "No"
			break
	print (ans)
	if nt!=t-1:
		input()