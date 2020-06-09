def f(n):
	s=str(n)
	count=0
	for i in s:
		count+=int(i)
	return count
n=int(input())
for i in range(n,n+10):
	if f(i)%4==0:
		print (i)
		exit(0)