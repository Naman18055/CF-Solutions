n,m = map(int,input().split())
a = list(map(int,input().split()))
l = {}
r = {}
minn = [i for i in range(n+1)]
maxx = [i for i in range(n+1)]
for i in range(1,n+1):
	l[i] = i
	r[i] = i

for i in a:
	if l[i] == 1:
		continue
	# print (l,r)
	l[i] -= 1
	l[r[l[i]]] += 1
	r[l[i]+1],r[l[i]] = r[l[i]],i
	# print (l,r)
	minn[i] = min(minn[i],l[i])
	maxx[r[l[i]+1]] = max(maxx[r[l[i]+1]],l[i]+1)

for i in range(1,n+1):
	print (minn[i],maxx[i])