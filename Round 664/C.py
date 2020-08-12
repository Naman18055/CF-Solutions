def found(i,j):
	for k in j:
		if k|i<=i:
			return True
	return False

n,m = map(int,input().split())
a = list(set(list(map(int,input().split()))))
b = list(set(list(map(int,input().split()))))
c = []
for i in a:
	c.append([])
	for j in b:
		c[-1].append(i&j)

for i in range(1024):
	flag = 0
	for j in c:
		if not found(i,j):
			flag = 1
			break
	if not flag:
		ans = i
		break
print (ans)