n=int(input())
x=2**(32)-1
stack=[]
for i in range(n):
	s=input()
	if len(stack)==0:
		if s=="add":
			stack.append("add 1")
		else:
			stack.append(s)
	else:
		if s=="end":
			if stack[-1][0]!="f":
				while stack[-2][0]=="a":
					temp4=stack.pop()
					num3=int(temp4.split()[-1])
					temp5=stack.pop()
					num4=int(temp5.split()[-1])
					if num3+num4>x:
						print ("OVERFLOW!!!")
						exit(0)
					stack.append("add "+str(num3+num4))
					#print (stack)
				temp=stack.pop()
				num=int(temp.split()[-1])
				temp2=stack.pop()
				num2=int(temp2.split()[-1])
				temp3=num*num2
				stack.append("add "+str(temp3))
				if temp3>x:
					print ("OVERFLOW!!!")
					exit(0)
			else:
				stack.pop()
		elif s=="add":
			if stack[-1][0:3]=="add":
				temp=stack.pop()
				num=int(temp.split()[-1])
				stack.append("add "+str(num+1))
				if num+1>x:
					print ("OVERFLOW!!!")
					exit(0)
			else:
				stack.append("add 1")
		else:
			stack.append(s)
ans=0
for i in stack:
	num=i.split()[-1]
	ans+=int(num)
	if ans>x:
		print ("OVERFLOW!!!")
		exit(0)
print(ans)
