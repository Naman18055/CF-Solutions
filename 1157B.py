n=int(input())
num=(input())
l=list(map(int,input().split()))
i=0
ans=""
while i<n:
	if int(num[i])<l[int(num[i])-1]:
		break
	else:
		ans+=num[i]
	i+=1
while i<n:
	if int(num[i])>l[int(num[i])-1]:
		break
	else:
		ans+=str(l[int(num[i])-1])
	i+=1
if i<n:
	ans+=num[i:]
print (ans)