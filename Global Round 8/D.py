import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
if n==1:
	print (a[0]**2)
	exit()
a.sort(reverse=True)
x = len(bin(a[0])[2:])
b = []
for i in range(n):
	y = bin(a[i])[2:]
	y = "0"*(x-len(y))+y
	b.append(list(y))
# for i in b:
# 	print (i)
for i in range(x):
	count = 0
	for j in range(n):
		if b[j][i]=="1":
			count += 1
	for j in range(count):
		b[j][i] = "1"
	for j in range(count,n):
		b[j][i] = "0"
# 	print (i,count,b)
# print (b)
ans = 0
for i in range(n):
	y = ""
	for j in range(x):
		y +=  b[i][j]
	ans += (int(y,2))**2
print (ans)
