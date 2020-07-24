def increment(s):
	i = len(s)-1
	while s[i]=="9":
		i -= 1
	s[i] = str(int(s[i])+1)
	for j in range(i+1,len(s)):
		s[j] = "0"
	return s

n,k = map(int,input().split())
s = input()
s = list(s)
ans = s[0:k]
for i in range(k,n):
	ans.append(ans[i-k])
if ans>=s:
	add = 0
	print (len(ans))
	print ("".join(map(str,ans)))
	exit()
else:
	ans = increment(s[0:k])
	for i in range(k,n):
		ans.append(ans[i-k])
	print (len(ans))
	print ("".join(map(str,ans)))