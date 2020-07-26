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

def matrix_expo(n):
	if n==1:
		return mat
	x = matrix_expo(n//2)
	if n%2:
		return multiply(mat,multiply(x,x))
	else:
		return multiply(x,x)

n = int(input())
if n==1:
	print (19)
	exit()
mat = [[0 for i in range(2)] for j in range(2)]
mat[0][0] = 13
mat[0][1] = 26
mat[1][0] = 0
mat[1][1] = 26

print (multiply(matrix_expo(n-1),[[19],[6]])[0][0])