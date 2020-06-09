import sys

def askquery(a,b):
	print (len(a),len(b),*a,*b)
	sys.stdout.flush()

for nt in range(int(input())):
	n=int(input())
	arr=[{} for i in range(7)]
	for i in range(1,n+1):
		b=bin(i)[2:]
		b="0"*(7-len(b))+b
		for j in range(7):
			if b[7-j-1]=="1":
				arr[j][i]=1
	ans=0
	# print (arr)
	for i in range(7):
		g1=[]
		g2=[]
		for j in range(1,n+1):
			if j in arr[i]:
				g1.append(j)
			else:
				g2.append(j)
		if len(g1)!=0 and len(g2)!=0:
			askquery(g1,g2)
			ans=max(ans,int(input()))
	print (-1,ans)
