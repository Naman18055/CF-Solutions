n=int(input())
ans=0
for i in range(n):
	s=input()
	if "+" in s:
		ans+=1
	else:
		ans-=1
print (ans)