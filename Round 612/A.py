for nt in range(int(input())):
	n=int(input())
	s=input()
	counts=[]
	count=0
	ind=s.find("A")
	if ind==-1:
		print (0)
		continue
	for i in range(ind,n):
		if s[i]=="A":
			counts.append(count)
			count=0
		else:
			count+=1
	counts.append(count)
	print (max(counts))