import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = [-1]*n
d = set(a)
done = {}
m = 0
while m in d:
	m += 1
b[0] = m
done[b[0]] = 1
for i in range(1,n):
	if a[i]==a[i-1]:
		curr = m+1
		while curr in d:
			curr += 1
		b[i] = curr
		done[b[i]] = 1
		m = max(m,b[i])
	else:
		if a[i-1] not in done:
			b[i] = a[i-1]
		else:
			curr = m+1
			while curr in d:
				curr += 1
			b[i] = curr
		done[b[i]] = 1
		m = max(m,b[i])

print (*b)