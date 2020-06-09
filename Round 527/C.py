n=int(input())
l=[]
count=0
longest=0
prefix=''
half=n-1
sol=[]
answer=''
for i in range((2*n-2)):
	l.append(input())
	for j in l:
		if len(j)==1:
			for k in l:
				if k.find(j)==0:
					count+=1
			if count>half:
				prefix=k
			break
	for j in l:
		if j.find(prefix)==0:
			if len(j)>longest:
				lprefix=j
	while half>0:
		for j in l:
			if lprefix.find(j)==0:
				sol.append("P")
			if lprefix.find(j)!=0:
				sol.append("S")
			half=half-1
for i in sol:
	answer+=i
print (answer)

