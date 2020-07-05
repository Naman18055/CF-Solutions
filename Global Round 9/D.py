from collections import Counter
def mex(arr,m):
	s = set(arr)
	ans = []
	i = 0
	while len(ans)!=m:
		if i not in s:
			ans.append(i)
		i += 1
	return ans[::-1]

def correct(arr):
	for i in range(1,n):
		if arr[i]<arr[i-1]:
			return False
	return True


for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	ans = []
	loc = {}
	# x = mex(a,n)
	# while x:
	# 	e = x.pop()
	# 	if e>=n or c[a[e]]==1:
	# 		break
	# 	else:
	# 		c[a[e]] -= 1
	# 		a[e] = e
	# 		ans.append(e+1)
	# x = []
	for i in range(n):
		if a[i] in loc:
			loc[a[i]][i] = 1
		else:
			loc[a[i]] = {i:1}

	for i in range(n):
		if a[i]!=i:
			minn = i
			break
	i = 0
	while not correct(a):
		x = mex(a,1)
		x = x[0]
		if x>=n:
			while a[minn]==minn:
				minn += 1
			for j in loc[minn]:
				a[j] = x
				ans.append(j+1)
				d = j
				break
			del loc[minn][d]
			if a[j] in loc:
				loc[a[j]][j] = 1
			else:
				loc[a[j]] = {j:1}
		else:
			del loc[a[x]][x]
			a[x] = x
			ans.append(x+1)
			if a[x] not in loc:
				loc[a[x]] = {x:1}
			else:
				loc[a[x]][x] = 1
		i += 1
		# print (a,loc,ans)
	print (len(ans))
	print (*ans)