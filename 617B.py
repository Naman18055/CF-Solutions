n = int(input())
a = list(map(int,input().split()))
if a.count(1)==1:
	print (1)
	exit()
elif a.count(1)==0:
	print (0)
	exit()
	
c = []
count = 1
for i in range(a.index(1)+1,n):
	if a[i]==1:
		c.append(count)
		count = 1
	else:
		count += 1
# print (c)
ans = 1
for i in c:
	ans = ans*i
print (ans)