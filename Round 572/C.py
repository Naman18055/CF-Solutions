n = int(input())
a = list(map(int,input().split()))
p = [a[0]]
for i in range(1,n):
	p.append(p[-1]+a[i])
for nt in range(int(input())):
	l,r = map(int,input().split())
	if l==1:
		print (p[r-1]//10)
	else:
		print ((p[r-1]-p[l-2])//10)