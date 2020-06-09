n=int(input())
points=[]
for i in range(n):
	points.append(list(map(int,input().split())))
selected = {}
ans = []
j = 0
k = 0
while len(selected)!=n:
	if j not in selected:
		first = points[j]
	else:
		j+=1
		continue
	if k not in selected and k!=j:
		second = points[k]
		temp = k
	else:
		k+=1
		continue
	for i in range(2,n):
		if i not in selected and i!=j:
			if min(first[0],second[0])<=points[i][0] and points[i][0]<=max(first[0],second[0]) and min(first[1],second[1])<=points[i][1] and points[i][1]<=max(first[1],second[1]) and min(first[2],second[2])<=points[i][2] and points[i][2]<=max(first[2],second[2]):
				second = points[i]
				temp = i
	selected[j]=1
	selected[temp]=1
	ans.append([j+1,temp+1])
	#print (ans)
for i in ans:
	print (i[0],i[1])
