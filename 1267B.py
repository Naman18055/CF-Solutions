s=input()
prev=s[0]
groups=[]
count=1
for i in range(1,len(s)):
	if s[i]!=prev:
		groups.append((prev,count))
		prev=s[i]
		count=1
	else:
		count+=1
groups.append((prev,count))
if not len(groups)%2:
	print (0)
	exit()
if groups[len(groups)//2][1]<2:
	print (0)
	exit()
flag=0
for i in range(len(groups)//2):
	if groups[i][0]!=groups[len(groups)-i-1][0]:
		flag=1
		break
	else:
		if groups[i][1]+groups[len(groups)-i-1][1]<3:
			flag=1
			break
if flag:
	print (0)
else:
	print (groups[len(groups)//2][1]+1)