n,k = map(int,input().split())
s = input()
if k==0:
	print (s)
	exit()
if n==1:
	print (0)
	exit()
ans = "1"
if ans[0]!=s[0]:
	k -= 1
for i in range(1,n):
	if k==0:
		ans+=s[i]
		continue
	ans+="0"
	if ans[-1]!=s[i]:
		k-=1
print (ans)
