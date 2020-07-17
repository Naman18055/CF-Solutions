def calc(i):
	if i!=0 and ord(s[i-1])==ord(s[i])-1:
		return True
	if i!=len(s)-1 and ord(s[i+1])==ord(s[i])-1:
		return True
	return False

n = int(input())
s = list(input())
ans = 0
for i in range(122,96,-1):
	j = 0 
	while j<len(s):
		if ord(s[j])==i and calc(j):
			ans += 1
			s.pop(j)
			j = max(0,j-1)
			# print (s,j)
		else:
			j += 1
print (ans)