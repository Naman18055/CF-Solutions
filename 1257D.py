import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	m=int(input())
	maxx={}
	for i in range(m):
		a,b=map(int,input().split())
		if b not in maxx:
			maxx[b]=a
		else:
			maxx[b]=max(a,maxx[b])
	arr=[]
	for i in maxx:
		arr.append([maxx[i],i])
	arr.sort(reverse=True)
	pref=[]
	prev=0
	# print (arr)
	for i in range(len(arr)):
		new=arr[i][1]
		if new>prev:
			for j in range(prev,new):
				pref.append(arr[i][0])
			prev=new
	# print (pref)
	if pref[0]<max(l):
		print (-1)
		continue
	m=0
	count=0
	day=0
	for i in range(n):
		m=max(m,l[i])
		count+=1
		if count>len(pref) or pref[count-1]<m:
			day+=1
			count=1
			m=l[i]
	print (day+1)