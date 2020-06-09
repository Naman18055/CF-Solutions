import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if n==1:
		print ("YES")
		continue
	new=[]
	for i in range(n):
		new.append(i+l[i%n])
	d={}
	ans="YES"
	for i in new:
		if i%n in d:
			ans="NO"
			break
		d[i%n]=1
	print (ans)