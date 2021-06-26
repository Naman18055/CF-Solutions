import sys
input = sys.stdin.readline

n, k, x = map(int,input().split())
a = sorted(list(map(int,input().split())))
b = []
for i in range(1, n):
	b.append((a[i]-a[i-1]-1)//x)
	if b[-1]<=0:
		b.pop()
b.sort()
i = 0
while i<len(b) and k>=b[i]:
	k -= b[i]
	i += 1
# print (a)
# print (b, i)
print (len(b)-i+1)
