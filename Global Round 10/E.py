import sys

def all_paths(i,j):
	if i==n-1 and j==n-1:
		return [[[i,j]]]
	elif i==n-1:
		b = all_paths(i,j+1)
		ans = []
		for k in b:
			ans.append([[i,j]]+k)
		return ans
	elif j==n-1:
		a = all_paths(i+1,j)
		ans = []
		for k in a:
			ans.append([[i,j]]+k)
		return ans
	else:
		a = all_paths(i+1,j)
		b = all_paths(i,j+1)
		ans = []
		for k in a:
			ans.append([[i,j]]+k)
		for k in b:
			ans.append([[i,j]]+k)
		return ans

def func(path):
	ans = 0
	for i in path:
		ans += mat[i[0]][i[1]]
	return ans

def maxx_path(i,j):
	start = [0,0]
	ans = 0
	while start[1]!=j:
		ans += mat[start[0]][start[1]]
		start[1] += 1

	while start[0]!=i-1:
		ans += mat[start[0]][start[1]]
		start[0] += 1
	ans += mat[start[0]][start[1]]
	start[1] += 1

	while start[0]!=n-1:
		ans += mat[start[0]][start[1]]
		start[0] += 1

	while start[1]!=n-1:
		ans += mat[start[0]][start[1]]
		start[1] += 1

	return ans

def minn_path(i,j):
	start = [0,0]
	ans = 0
	while start[1]!=j:
		ans += mat[start[0]][start[1]]
		start[1] += 1

	while start[0]!=i:
		ans += mat[start[0]][start[1]]
		start[0] += 1

	while start[1]!=n-1:
		ans += mat[start[0]][start[1]]
		start[1] += 1

	while start[0]!=n-1:
		ans += mat[start[0]][start[1]]
		start[0] += 1

	return ans



def construct():
	for i in range(n-2,-1,-1):
		for j in range(1,n):
			s1 = maxx_path(j,i)
			s2 = minn_path(j,i)
			mat[j][i] = s1-s2+1

def calc(i,j):
	start = curr[::]
	a1 = a2 = 0
	while start[1]!=j:
		start[1] += 1
		a1 += mat[start[0]][start[1]]
	a2 = a1 + mat[i][j]
	a1 = a2
	start[0] += 1

	while start[0]!=n-1:
		start[0] += 1
		a1 += mat[start[0]][start[1]]

	while start[1]!=n-1:
		start[1] += 1
		a1 += mat[start[0]][start[1]]

	return a1,a2

def print_path(a,b):
	start = a[::]
	while start[1] != b[1]:
		start[1] += 1
		print (start[0]+1,start[1]+1)

	if start[0]!=b[0] or start[1]!=b[1]:
		print (b[0]+1,b[1]+1)


n = int(input())
mat = [[0 for i in range(n)] for j in range(n)]
construct()
for i in mat:
	print (*i)
sys.stdout.flush()

# col = [0]*n
# for i in range(n-2,-1,-1):
# 	s = 0
# 	for j in range(n):
# 		s += mat[j][i]
# 	col[i] = col[i+1]+s
# print (*col)
# curr = [0,0]
# print (calc(curr[0]+1,n-1))

q = int(input())
for nt in range(q):
	k = int(input())
	curr = [0,0]
	ans = [[0,0]]
	left = k
	while curr[0]!=n-1:
		for i in range(n-1,curr[1]-1,-1):
			s,d = calc(curr[0]+1,i)
			# print (curr,s,d,i,left)
			if s>=left:
				left -= d
				curr = [curr[0]+1,i]
				ans.append([curr[0],curr[1]])
				break

	if ans[-1][0]!=n-1 or ans[-1][1]!=n-1:
		ans.append([n-1,n-1])

	print (ans[0][0]+1,ans[0][1]+1)
	for i in range(1,len(ans)):
		print_path(ans[i-1],ans[i])

	sys.stdout.flush()
