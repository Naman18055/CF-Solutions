import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = ["a"*(a[0])]
	x = 1
	for i in range(1,n):
		ans.append(ans[-1][0:a[i-1]]+chr(x+97)*(max(0,a[i]-a[i-1])))
		x += 1
		x = x%20
	ans.append(ans[-1][0:a[-1]])
	for i in range(n+1):
		if len(ans[i])==0:
			if i==0 or ans[i-1][0]=="x":
				ans[i] = "y"
			else:
				ans[i] = "x"
	for i in ans:
		print (i)