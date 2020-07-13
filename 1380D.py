n,m = map(int,input().split())
x,k,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
if a==b:
	print (0)
	exit()
s = set(b)
i = 0
j = 0
while i<n and j<m:
	if a[i]==b[j]:
		i += 1
		j += 1
	else:
		i += 1
if j!=m:
	print (-1)
	exit()

rem = [[]]
occ = []
for i in range(n):
	if a[i] not in s:
		rem[-1].append(a[i])
	else:
		rem[-1].sort(reverse=True)
		rem.append([])
		occ.append(i)
rem[-1].sort(reverse=True)
maxa = max(rem)
maxb = max(b)

# print (rem)
# print (occ)

if k*y<=x:
	cost = 0
	for i in range(len(rem)-1):
		if len(rem[i])==0:
			continue
		j = 0
		if rem[i][j]>max(a[occ[i-1 if i>0 else 0]],a[occ[i]]):
			cost += x
			j += k
			if j>len(rem[i]):
				print (-1)
				exit()
		cost += (len(rem[i])-j)*y

	j = 0
	if rem[-1][0]>a[occ[-1]]:
		cost += x
		j += k
		if j>len(rem[-1]):
			print (-1)
			exit()
	cost += (len(rem[-1])-j)*y
	print (cost)
else:
	cost = 0
	d = occ[0]
	if d!=0 and d<k:
		if a[occ[0]]<max(a[0:occ[0]]):
			print (-1)
			exit()
	cost += (x*(d//k)+y*(d%k))

	for i in range(1,len(occ)):
		d = occ[i]-occ[i-1]-1
		if d!=0 and d<k:
			if max(a[occ[i]],a[occ[i-1]])<max(a[occ[i-1]+1:occ[i]]):
				print (-1)
				exit()
		cost += (x*(d//k)+y*(d%k))
	# print(cost)
	d = n-occ[-1]-1
	if d!=0 and d<k:
		if a[occ[-1]]<max(a[occ[-1]+1:]):
			print (-1)
			exit()
	cost += (x*(d//k)+y*(d%k))

	print (cost)
