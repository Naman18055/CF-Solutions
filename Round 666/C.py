def euclidean_algo(a,b):
	if not a:
		return 0,1,b
	x,y,gcd = euclidean_algo(b%a,a)
	return y-(b//a)*x,x,gcd

n = int(input())
a = list(map(int,input().split()))
if n==1:
	print (1,1)
	print (-a[0])
	print (1,1)
	print (0)
	print (1,1)
	print (0)
	exit()
if n==2:
	print (1,1)
	print (-a[0])
	print (2,2)
	print (-a[1])
	print (1,1)
	print (0)
	exit()

if True:
	num = n-1
	print (1,n-1)
	x,y,z = euclidean_algo(n,n-1)
	for i in range(n-1):
		print (-((n-1)*y*a[i]),end=" ")
		a[i] -= ((n-1)*y*a[i])
	print ()
	print (n,n)
	print (-a[-1])
	a[-1] = 0
	print (1,n)
	for i in range(n):
		print (-a[i],end=" ")
	print ()
