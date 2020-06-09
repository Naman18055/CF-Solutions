n=int(input())
l=[]
for i in range(n):
	l.append(list(map(int,input().split())))
k=int(input())
for i in range(n):
	if k<=l[i][-1]:
		print (n-i)
		break