t=int(input())
for nt in range(t):
	n,r=map(int,input().split())
	l=list(map(int,input().split()))
	l=list(set(l))
	l.sort(reverse=True)
	stack=[l[0]]
	count=1
	for i in range(1,len(l)):
		stack.pop()
		if l[i]-count*r>0:
			stack.append(l[i])
			count+=1
		else:
			break
	print (count)
