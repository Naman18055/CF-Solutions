n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
p1 = [a[0]]
p2 = [b[0]]
for i in range(1,n):
	p1.append(p1[-1]+a[i])
	p2.append(p2[-1]+b[i])
# print (p1,p2)
for i in range(int(input())):
	x,y,z = map(int,input().split())
	if x==1:
		if y==1:
			print (p1[z-1])
		else:
			print (p1[z-1]-p1[y-2])
	else:
		if y==1:
			print (p2[z-1])
		else:
			print (p2[z-1]-p2[y-2])