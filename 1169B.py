# import sys
# input = sys.stdin.readline
def common(a,b):
	flag = 0
	for i in a:
		if i in b:
			flag = 1
			num = i
			break
	if not flag:
		return -1
	return num

n,m = map(int,input().split())
if m<=2:
	print ("YES")
	exit()
a = []
for i in range(m):
	a.append(tuple(map(int,input().split())))
a = list(set(a))
n = len(a)
if n<=2:
	print ("YES")
	exit()
ans = "NO"
for i in range(2):
	x1 = a[0][i]
	t = []
	for j in range(1,n):
		if x1 not in a[j]:
			t.append(a[j])
	if len(t)<=1:
		ans = "YES"
		break
	c = common(t[1],t[0])
	if c==-1:
		continue
	flag = 0
	for j in range(2,len(t)):
		if c!=common(t[j],t[j-1]):
			flag = 1
			break
	if not flag:
		ans = "YES"
		break
print (ans)