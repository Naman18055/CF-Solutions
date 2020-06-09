import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
d = {}
for i in range(n):
	d[b[i]] = i+1
x = 0
ans = n
for i in range(n):
	if d[a[i]]>x:
		x = d[a[i]]
		ans -= 1
print (ans)