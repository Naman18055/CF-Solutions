l=[]
for i in range(2,35):
	l.append((2**i)-1)
# print (l)
for nt in range(int(input())):
	n=int(input())
	flag=0
	for i in l:
		if n%i==0:
			print (n//i)
			flag=1
			break
