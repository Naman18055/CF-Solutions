s=input()
d=["A","H","I","M","O","T","U","V","W","X","Y"]
d=set(d)
ans="YES"
for i in s:
	if i not in d:
		ans="NO"
		break
if s!=s[::-1]:
	ans="NO"
print (ans)