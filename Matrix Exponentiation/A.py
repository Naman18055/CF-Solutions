def multiply(a,b):
	ans = []
	for i in range(len(a)):
		ans.append([])
		for j in range(len(b[0])):
			s = 0
			for k in range(len(a[i])):
				s += (a[i][k]*b[k][j])
			ans[-1].append(s)
	return ans

def matrix_expo(n):
	if n==1:
		return mat
	x = matrix_expo(n//2)
	if n%2:
		return multiply(mat,multiply(x,x))
	else:
		return multiply(x,x)

n,p = map(float,input().split())
n = int(n)
if not n:
	print (1)
	exit()

mat = [[0 for i in range(2)] for j in range(2)]
mat[0][0] = 1-2*p
mat[0][1] = 1
mat[1][1] = 1

print (multiply(matrix_expo(n),[[1],[p]])[0][0])