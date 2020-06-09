n = int(input())
s = input()
o,c = 0,0
for i in s:
	if i=="(":
		o+=1
	else:
		c+=1
if o!=c:
	print (-1)
	exit()
stk = [s[0]]
if s[0]=="(":
	o = 1
	c = 0
else:
	o = 0
	c = 1
ans = 0
for i in range(1,n):
	if s[i]==")" and (len(stk)>0 and stk[-1]=="("):
		stk.pop()
		c+=1
	elif s[i]==")":
		stk.append(s[i])
		c+=1
	elif s[i]=="(":
		stk.append(s[i])
		o+=1
	if len(stk)==0:
		o,c = 0,0
	# print (stk,o,c)
	if o==c:
		ans+=(2*o)
		o = 0
		c = 0
		stk=[]
print (ans)