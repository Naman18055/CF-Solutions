import random
n,m = 25,23
mat = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
	for j in range(m):
		x = random.randint(1,100)
		if x<=2:
			mat[i][j] = 1
X = mat

if True:
	mid = []
	if (n+m)%2==0:
		mid = [(n+m-1)//2]
	ans = 0
	count = {}
	for i in range(n):
		for j in range(m):
			if i+j not in count:
				o,z = 0,0
				s = (i,j)
				while s[0]<n and s[1]>=0:
					if mat[s[0]][s[1]]==1:
						o+=1
					else:
						z+=1
					s = (s[0]+1,s[1]-1)
				s = (i-1,j+1)
				while s[0]>=0 and s[1]<m:
					if mat[s[0]][s[1]]==1:
						o+=1
					else:
						z+=1
					s = (s[0]-1,s[1]+1)
				count[(i+j)] = (z,o)
	# print (count)
	for i in count:
		if i not in mid:
			ans += min(count[i][0]+count[n+m-i-2][0],count[i][1]+count[n+m-i-2][1])
			# print (i,ans)

	print (ans//2)

def F(t,z,S,E,X):
	i = t[0]
	j = t[1]
	if z == 1:
		if i+1<n:
			S[(i+1,j)]=X[i+1][j]
		if j+1<m:
			S[(i,j+1)]=X[i][j+1]
	if z == -1:
		if i-1>-1:
			E[(i-1,j)]=X[i-1][j]
		if j-1>-1:
			E[(i,j-1)]=X[i][j-1]
 
 
if True:
	c = 0
	S = {}
	E = {}
	S[(0,0)]=X[0][0]
	E[(n-1,m-1)]=X[n-1][m-1]
	L = S
	R = E
	while S!=E and L!=E:
		a = 0
		for s in S:
			a += S[s]
		b = 0
		for e in E:
			b += E[e]
		c = c + min(a+b,len(S)+len(E)-a-b)
 
		P = {}
		Q = {}
		for s in S:
			F(s,1,P,Q,X) 
		for e in E:
			F(e,-1,P,Q,X)
		L = S
		R = E
		S = P
		E = Q
 
	print(c) 
