import sys
input = sys.stdin.readline

def calc(a):
	ans = a[0]+a[-1]
	for i in range(1, n):
		ans += abs(a[i]-a[i-1])
	return ans


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if n==1:
		print (a[0])
		continue

	ans = 0
	if a[0]>a[1]:
		ans += a[0]-a[1]
		a[0] = a[1]
	if a[-1]>a[-2]:
		ans += a[-1]-a[-2]
		a[-1] = a[-2]

	for i in range(1, n-1):
		if a[i]>a[i-1] and a[i]>a[i+1]:
			ans += min(a[i]-a[i-1], a[i]-a[i+1])
			a[i] = max(a[i-1], a[i+1])
	print (ans+calc(a))