import math
n=int(input())
l=list(map(int,input().split()))
x=int(math.log(n,2))
a=n
#print (x)
if l==sorted(l):
	print (n)
else:
	#print (1)
	for i in range(x):
		#print (2)
		if l[0:a//2]==sorted(l[0:a//2]):
			#print (3)
			a=a//2
			break
		if l[a//2:]==sorted(l[a//2:]):
			# print (l[a//2:0])
			# print (4)
			a=a//2
			break
		a=n//2
		#print (a)
	print (a)


