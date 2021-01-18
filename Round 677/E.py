n = int(input())
a, b= 1, 1
for i in range(1,n+1):
	a = a*i
for i in range(1,n//2+1):
	b = b*i
ans = (a//(b*b))//2
c = 1
for i in range(1,n//2):
	c = c*i
ans = ans*c*c
print (ans)