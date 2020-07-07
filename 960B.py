import sys
input = sys.stdin.readline
n,k1,k2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [abs(a[i]-b[i]) for i in range(n)]
k = k1 + k2
while k!=0:
	maxx = 0
	for i in c:
		maxx = max(i,maxx)
	if maxx==0:
		break
	for i in range(n):
		if c[i]==maxx:
			c[i] -= 1
			k -= 1
		if k==0:
			break
ans = 0
for i in c:
	ans += i**2
print (ans+k%2)