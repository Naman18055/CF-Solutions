import sys
mod = 10**9+7
input = sys.stdin.readline

def calc(x):
	return (x*(x-1))//2

for nt in range(int(input())):
	n, m, k = map(int,input().split())
	a = list(map(int,input().split()))
	a.sort()
	i, j = 0, 0
	b = sorted(set(a))
	ans = 0
	# print (a)
	# print (b)
	while i<len(a):
		while j<n and a[j]-a[i]<=2:
			j += 1
		if (j-i-1)>=2:
			ans += calc(j-i-1)
		i += 1

	print (ans)
