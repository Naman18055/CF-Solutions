s = input()
n = len(s)
ans = "YES"
for i in range(n-2):
	# print (ord(s[i]) + ord(s[i+1])-128, ord(s[i+2])-63)
	if (ord(s[i])+ord(s[i+1])-129)%26+1!=ord(s[i+2])-63:
		ans = 'NO'
		break
print (ans)