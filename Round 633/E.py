s=[]
d={}
a,b,c=-1,-1,-1
while len(s)!=100:
	for i in range(1,100):
		if i not in d:
			a=i
			flag=0
			for j in range(a+1,100):
				if j not in d:
					b=j
					for k in range(b+1,100):
						if k not in d and a^b^k==0:
							s.append(a)
							s.append(b)
							s.append(k)
							d[a]=1
							d[b]=1
							d[k]=1
							flag=1
					if flag==1:
						break
			if flag==1:
				break
	if s[-1]==99:
		break
print (s)

