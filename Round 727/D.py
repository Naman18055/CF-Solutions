import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))
items = 0
a.sort(key = lambda x : x[1])
i = 0
j = n-1
s = sum([a[i][0] for i in range(n)])
ans = 0
while items < s:
	if items>=a[i][1]:
		ans += a[i][0]
		items += a[i][0]
		a[i][0] = 0
		i += 1
	else:
		if a[j][0]>=a[i][1]-items:
			ans += 2*(a[i][1]-items)
			a[j][0] -= (a[i][1]-items)
			items = a[i][1]
		else:
			ans += 2*a[j][0]
			items += a[j][0]
			a[j][0] = 0
			j -= 1
	# print (a, items, ans)
print (ans)

