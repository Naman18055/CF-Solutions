n = int(input())
n = str(n)
ans = 0
for i in n:
	ans += int(i)
if len(n)==1:
	print (n)
else:
	print (int((int(n)**0.5)%10))