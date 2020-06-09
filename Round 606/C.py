t=int(input())
for nt in range(t):
	s=input()
	i=0
	count=0
	ans=[]
	while i<len(s)-2:
		if s[i]=="t" and s[i+1]=="w" and s[i+2]=="o" and i+4>=len(s):
			count+=1
			ans.append(i+2)
			break
		elif s[i]=="t" and s[i+1]=="w" and s[i+2]=="o" and s[i+3]=="n" and s[i+4]=="e":
			count+=1
			ans.append(i+3)
			i+=5
		elif s[i]=="t" and s[i+1]=="w" and s[i+2]=="o":
			count+=1
			ans.append(i+2)
			i+=3
		elif s[i]=="o" and s[i+1]=="n" and s[i+2]=="e":
			count+=1
			ans.append(i+2)
			i+=3
		else:
			i+=1
	print (count)
	print (*ans)


