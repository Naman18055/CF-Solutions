def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

for nt in range(int(input())):
	n=int(input())
	l=list_input()
	ans="Yes"
	k=1
	locations={}
	for i in range(n):
		locations[l[i]]=i
	covered=n
	while k<n+1:
		ind=locations[k]
		# print (ind,covered)
		for i in range(ind,covered):
			if l[i]!=k:
				ans="No"
				break
			k+=1
			# print (l,i,k)
		if ans=="No":
			break
		else:
			covered=ind
	print (ans)