def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n,k=mult_input()
	l=list_input()
	s=list(set(l))
	if len(s)>k:
		print (-1)
	else:
		d={}
		ans=[]
		for i in range(n):
			if l[i] not in d:
				ans.append(l[i])
				d[l[i]]=1
			if len(ans)==k:
				break
		while len(ans)!=k:
			ans.append(1)
		print (k*(100))
		print (*(ans*(100)))