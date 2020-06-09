n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
v = [[0,0] for i in range(n)]
s = [0 for i in range(n)]
s[-1] = a[-1] + b[-1]
for i in range(n-2,-1,-1):
	s[i] = s[i+1] + a[i] + b[i]
v[-1][0] = b[-1]
v[-1][1] = a[-1]
s1, s2 = b[-1], a[-1]
for i in range(n-2,-1,-1):
	v[i][0] = v[i+1][0] + s1 + a[i+1] + b[i]*(2*(n-i)-1)
	v[i][1] = v[i+1][1] + s2 + b[i+1] + a[i]*(2*(n-i)-1)
	s1 += a[i+1] + b[i]
	s2 += b[i+1] + a[i]
ans = v[0][0]
turn = 1
for i in range(n):
	if i%2:
		ans = max(ans, v[i+1][0]+s[i]*(2*(i+1)))
	else:
		ans = max(ans, v[i][0]+s[i]*(2*i+j))
	print (v[i][j]+s[i]*(2*i+j))
print (ans)