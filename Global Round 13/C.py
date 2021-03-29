import sys
input = sys.stdin.readline

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	ans = 0
	c = [0]*n
	for i in range(n):
		if a[i]>c[i]+1:
			ans += (a[i]-c[i]-1)
			c[i] += (a[i]-c[i]-1)
		if i!=n-1:
			c[i+1] += c[i]-a[i]+1
			
		for j in range(min(i+a[i], n-1), i+1, -1):
			c[j] += 1
		# print (c)
				
			
	print (ans)


