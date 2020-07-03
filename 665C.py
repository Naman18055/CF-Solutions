s = input()
n = len(s)
if n==1:
	print (s[0])
	exit()
	
ans = s[0]
for i in range(1,n-1):
	if s[i]==ans[i-1]:
		if ans[i-1]=="a" or s[i+1]=="a":
			if ans[i-1]=="b" or s[i+1]=="b":
				ans += "c"
			else:
				ans += "b"
		else:
			ans += "a"
	else:
		ans += s[i]
if s[-1]==ans[-1]:
	if ans[-1]=="a":
		ans += "b"
	else:
		ans += "a"
else:
	ans += s[-1]
print (ans)