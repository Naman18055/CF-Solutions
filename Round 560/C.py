n=int(input())
s=input()
ans=" "
for i in range(n):
	if len(ans)%2==0:
		if s[i]!=ans[-1]:
			ans+=s[i]
	else:
		ans+=s[i]
ans=ans[1:]
if len(ans)%2==0:
	print (n-len(ans))
	print (ans)
else:
	print (n-len(ans)+1)
	print (ans[0:-1])