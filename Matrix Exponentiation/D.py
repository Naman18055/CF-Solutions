mod = 10**9+7

def multiply(a,b):
	ans = []
	for i in range(len(a)):
		ans.append([])
		for j in range(len(b[0])):
			s = 0
			for k in range(len(a[i])):
				s += (a[i][k]*b[k][j])%mod
			ans[-1].append(s%mod)
	return ans

def exp(n):
	if n==1:
		return mat
	x = exp(n//2)
	if n%2:
		return multiply(mat,multiply(x,x))
	else:
		return multiply(x,x)

n,m,k = map(int,input().split())
graph = [[] for i in range(n)]
incoming = [[] for i in range(n)]
for i in range(m):
	x,y = map(int,input().split())
	graph[x-1].append(y-1)
	incoming[y-1].append(x-1)

a = []
for i in incoming:
	a.append([len(i)])

if k==1:
	print (m)
	exit()

mat = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
	for j in incoming[i]:
		mat[i][j] = 1
# for i in mat:
# 	print (*i)
# for i in a:
# 	print (*i)

ans = multiply(exp(k-1),a)
res = 0
for i in ans:
	res += sum(i)
print (res%mod)