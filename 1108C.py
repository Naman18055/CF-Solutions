def diff(a,b):
	count=0
	for i in range(len(a)):
		if a[i]!=b[i]:
			count+=1
	return count

def create(a,n):
	ans=a*(n//3)
	temp=n-len(ans)
	ans=ans+a[0:temp]
	return ans

n=int(input())
s=input()
m=1000000000
if n>=3:
	temp="RGB"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	temp="RBG"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	temp="GBR"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	temp="GRB"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	temp="BRG"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	temp="BGR"
	new=create(temp,n)
	temp2=diff(new,s)
	if temp2<m:
		m=temp2
		ans=new
	print (m)
	print (ans)
else:
	if n==1:
		print (0)
		print (s)
	elif n==2:
		if s[0]!=s[1]:
			print (0)
			print (s)
		else:
			print (1)
			if s[0]=="R":
				print ("RB")
			elif s[0]=="B":
				print ("BR")
			else:
				print ("GB")