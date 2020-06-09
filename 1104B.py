s=input()
n=len(s)
stack=[s[0]]
count=0
for i in range(1,n):
	if len(stack)>0:
		if s[i]==stack[-1]:
			stack.pop()
			count+=1
		else:
			stack.append(s[i])
	else:
		stack.append(s[i])
if count%2==0:
	print ("NO")
else:
	print ("YES")
