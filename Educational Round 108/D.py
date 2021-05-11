import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = sum([a[i]*b[i] for i in range(n)])
ans = s

for i in range(n):
	for j in range(i-1, i+1):
		temp = s
		k = i+1
		while j>=0 and k<n:
			temp -= (a[j] - a[k]) * (b[j] - b[k])
			ans = max(ans, temp)
			j -= 1
			k += 1

print (ans)
