from collections import Counter

import sys
input = sys.stdin.readline

def check(ind, done):
	i = 1
	x = a[0]
	ans = [[a[0], ind]]

	while i<2*n:
		# print (done, x, ind, c)
		if done[a[i]] == og[a[i]]:
			i += 1
			continue

		y = x - a[i]
		c[a[i]] -= 1
		done[a[i]] += 1
		if not c[a[i]]:
			del c[a[i]]

		if y not in c:
			return "NO"

		c[y] -= 1
		done[y] += 1
		ans.append([a[i], y])
		if not c[y]:
			del c[y]
		x = a[i]
		i += 1

	return ans

for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort(reverse = True)
	# print (a)
	og = Counter(a)
	x = a[0]

	for i in range(1, 2*n):
		c = Counter(a[1:])
		done = {}
		for j in a:
			done[j] = 0
		done[a[0]] += 1
		done[a[i]] += 1
		c[a[i]] -= 1
		if not c[a[i]]:
			del c[a[i]]
		ans = check(a[i], done)
		# print (ans)
		if ans!="NO":
			break
	

	if ans == "NO":
		print (ans)
		continue
	for i in c:
		ans[0][1] = i
	print ("YES")
	print (sum(ans[0]))
	for i in ans:
		print (*i)



