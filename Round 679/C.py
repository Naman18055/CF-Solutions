import sys
input = sys.stdin.readline

a = sorted(list(map(int,input().split())))[::-1]
n = int(input())
b = list(map(int,input().split()))
arr = []
for i in range(n):
	for j in a:
		arr.append((b[i]-j, i))
arr.sort()
ans, maxx, minn = 10**18, 0, 10**18
l, r = 0, 0
d, covered = {}, set()
for i in range(n):
	d[i] = 0
while r<len(arr):
	covered.add(arr[r][1])
	d[arr[r][1]] += 1
	if len(covered)!=n:
		r += 1
	else:
		while len(covered)==n:
			ans = min(ans, arr[r][0]-arr[l][0])
			d[arr[l][1]] -= 1
			if d[arr[l][1]]==0:
				covered.remove(arr[l][1])
				break
			l += 1
print (ans)



