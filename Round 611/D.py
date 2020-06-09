n,m=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
new=[l[0]]
for i in range(1,n-1):
	if l[i+1]-l[i-1]!=2:
		new.append(l[i])
new.append(l[-1])
d={}
for i in l:
	d[str(i)]=1
ans=[]
minans=l[0]
maxans=l[-1]
dist=1
count=0
while (maxans-minans+1)>(len(ans)+n) and len(ans)<m:
	for i in range(len(new)):
		if str(new[i]-dist) not in d:
			ans.append(new[i]-dist)
			d[str(new[i]-dist)]=1
			if new[i]-dist<minans:
				minans=new[i]-dist
			count+=dist
		if str(new[i]+dist) not in d:
			ans.append(new[i]+dist)
			d[str(new[i]+dist)]=1
			if new[i]+dist>maxans:
				maxans=new[i]+dist
			count+=dist
	new1=[new[0]]
	for i in range(1,len(new)-1):
		if str(new[i+1]) in d and str(new[i-1]) in d:
			new1.append(new[i])
	new1.append(new[-1])
	new=[]
	for i in range(len(new1)):
		new.append(new1[i])
	#print (d,dist,ans)
	dist+=1
if len(ans)>m:
	print (count-((dist-1)*(len(ans)-m)))
	for i in range(m):
		print (ans[i],end=" ")
	print ()
elif len(ans)==m:
	print (count)
	print (*ans)
else:
	if len(ans)>0:
		left = min(ans)
		right = max(ans)
	else:
		left = l[0]
		right = l[-1]
	rem = m-len(ans)
	dist=1
	if rem%2==0:
		for i in range(rem//2):
			ans.append(left-dist)
			dist+=1
			count+=abs(ans[-1]-l[0])
		dist=1
		for i in range(rem//2):
			ans.append(right+dist)
			dist+=1
			count+=abs(ans[-1]-l[-1])
	else:
		for i in range(rem//2):
			ans.append(left-dist)
			dist+=1
			count+=abs(ans[-1]-l[0])
		dist=1
		for i in range(rem//2+1):
			ans.append(right+dist)
			dist+=1
			count+=abs(ans[-1]-l[-1])
	print (count)
	print (*ans)