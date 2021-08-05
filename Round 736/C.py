import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ans = [0]*n
count = n
for i in range(m):
	u, v = map(int,input().split())
	if u<v:
		ans[u-1] += 1
		if ans[u-1]==1:
			count -= 1
	else:
		ans[v-1] += 1
		if ans[v-1]==1:
			count -= 1
	
for i in range(int(input())):
	query = list(map(int,input().split()))
	if query[0]==3:
		print (count)
	elif query[0]==1:
		u, v = query[1:]
		if u<v:
			ans[u-1] += 1
			if ans[u-1]==1:
				count -= 1
		else:
			ans[v-1] += 1
			if ans[v-1]==1:
				count -= 1
	else:
		u, v = query[1:]
		if u<v:
			ans[u-1] -= 1
			if ans[u-1]==0:
				count += 1
		else:
			ans[v-1] -= 1
			if ans[v-1]==0:
				count += 1



