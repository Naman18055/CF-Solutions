import sys
input = sys.stdin.buffer.readline
def list_input():
	return list(map(int,input().split()))
def mult_input():
	return map(int,input().split())

for nt in range(int(input())):
	n=int(input())
	l=list_input()
	if n==1:
		print (1)
		continue
	elif n==2:
		if l[0]==l[1]:
			print (2)
		else:
			print (1)
		continue
	if len(set(l))==n:
		print (1)
		continue
	counts=[[0 for i in range(n)] for j in range(200)]
	d={}
	for i in range(1,201):
		count=0
		d[i]={}
		for j in range(n):
			if l[j]==i:
				count+=1
				d[i][count]=j
			counts[i-1][j]=count
	# for i in range(26):
	# 	print (*counts[i])
	ans=0
	for i in range(1,201):
		for j in range(1,201):
			start=0
			end=n-1
			# first=0
			for k in range(len(d[i])//2):
				first=d[i][k+1]
				second=d[i][(counts[i-1][-1]-k)]
				ans=max(ans,2*(k+1)+counts[j-1][second-1]-counts[j-1][first])

			# while start<end:
			# 	# print (i,j,start,end)
			# 	if l[start]==i and l[end]==i:
			# 		first+=1
			# 		second=(counts[j-1][end-1]-counts[j-1][start])
			# 		# print (i,j,first,second)
			# 		ans=max(first*2+second,ans)
			# 		start+=1
			# 		end-=1
			# 	elif l[start]==i:
			# 		end-=1
			# 	elif l[end]==i:
			# 		start+=1
			# 	else:
			# 		end-=1
			# 		start+=1
	print (ans)

