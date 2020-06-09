def calc(d):
	return int(((1+4*d)**0.5)//2)
t=int(input())
for nt in range(t):
	a,b=map(int,input().split())
	a,b=max(a,b),min(a,b)
	d=a-b
	if d%2==0:
		i=calc(2*d)
		while True:
			if (i**2+i)%4==0 and (i**2+i-2*d)>=0:
				print (i)
				break
			i+=1
	else:
		i=calc(2*d)
		while True:
			if (i**2+i)%4==2 and (i**2+i-2*d)>=0:
				print (i)
				break
			i+=1
	#n^2+n-2*d/4

