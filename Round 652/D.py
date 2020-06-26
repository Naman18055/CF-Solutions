
mod = 10**9+7
a = [0,0,1,1]
X = 2000001
while len(a)<X:
	a.append((a[-1]+2*a[-2])%mod)
b = [[0],[0],[1]]
for i in range(3,X):
	b[i%3].append((b[i%3][-1]+a[i])%mod)
# print (a)
# for i in b:
# 	print (*i)
for nt in range(int(input())):
	n = int(input())
	print ((b[n%3-1][(n-1)//3]*4)%mod)

