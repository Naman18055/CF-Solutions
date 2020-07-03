def check(b):
	for i in b:
		for j in b:
			if (a[i],a[j]) in pair or (a[j],a[i]) in pair:
				return False
	return True

n,m = map(int,input().split())
a = []
ind = {}
for i in range(n):
	a.append(input())
	ind[a[-1]] = i
graph = [[] for i in range(n)]
pair = {}
for i in range(m):
	x,y = input().split()
	pair[(x,y)] = 1
	graph[ind[x]].append(ind[y])
	graph[ind[y]].append(ind[x])
if m==0:
	print (n)
	a.sort()
	for i in a:
		print (i)
	exit()

ans = 0
string = ""
for i in range(1,2**n):
	b = bin(i)[2:]
	b = "0"*(n-len(b))+b
	temp = []
	for j in range(n):
		if b[j]=="1":
			temp.append(ind[a[j]])
	# print (i,b,temp,check(temp),pair,ind)
	if check(temp):
		if len(temp)>ans:
			ans = len(temp)
			string = b
print (ans)
ansl = []
for i in range(n):
	if string[i]=="1":
		ansl.append(a[i])
ansl.sort()
for i in ansl:
	print (i)
