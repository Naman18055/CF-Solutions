n=int(input())
s=input()
stack=[]
queue=[]
ans=[-1]*n
old=0
new=0
flag=0
for i in range(n):
	if s[i]=="(":
		if len(stack)==0:
			stack.append(s[i])
			old=i
		else:
			queue.append([i,s[i]])
	elif s[i]==")":
		stack.pop()
		ans[i]=flag
		ans[old]=flag
		if flag==0:
			flag=1
		else:
			flag=0
	if len(stack)==0:
		if len(queue)>0:
			old=queue[0][0]
			stack.append((queue.pop(0))[1])
sol=""
for i in ans:
	if i==0:
		sol+="0"
	else:
		sol+="1"
print (sol)
