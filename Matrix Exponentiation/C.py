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


n = int(input())
if n==0:
	print (0)
	exit()
elif n==1:
	print (1)
	exit()
mat = [[1 for i in range(2)] for j in range(2)]
mat[1][1] = 0
print (multiply(exp(n),[[0],[1]])[0][0])