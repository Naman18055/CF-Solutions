mod = 4294967296 
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

def reach(a,b):
	if a==b:
		return False
	if (abs(a[0]-b[0])==2 and abs(a[1]-b[1])==1) or (abs(a[0]-b[0])==1 and abs(a[1]-b[1])==2):
		return True
	return False

k = int(input())
if k==1:
	print (3)
	exit()
elif k==0:
	print (1)
	exit()
a = []
for i in range(65):
	a.append([0])
a[10][0] = a[17][0] = a[0][0] = a[-1][0] = 1

mat = [[0 for i in range(65)] for j in range(65)]
for i1 in range(8):
	for j1 in range(8):
		for i2 in range(8):
			for j2 in range(8):
				if reach((i1,j1),(i2,j2)):
					mat[i1*8+j1][i2*8+j2] = 1
mat[0][-1] = mat[-1][-1] = 1
ans = multiply(exp(k-1),a)
res = 0
# print (ans)
for i in ans:
	res += sum(i)
	res = res%mod
print ((res-1)%mod)