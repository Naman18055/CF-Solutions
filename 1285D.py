def solve(group,bit):
	# print (group,bit,x)
	if bit==t-1:
		for i in range(1,len(group)):
			if group[i][bit]!=group[0][bit]:
				# x.append("1")
				return 1
		# x.append(group[0][bit])
		return 0
	g0,g1=[],[]
	for i in range(len(group)):
		if int(group[i][bit]):
			g1.append(group[i])
		else:
			g0.append(group[i])
	if len(g0)==0:
		# ans.append("0")
		x.append("1")
		return solve(g1,bit+1)
	elif len(g1)==0:
		# ans.append("0")
		x.append("0")
		return solve(g0,bit+1)
	else:
		s1=solve(g0,bit+1)
		s2=solve(g1,bit+1)
		# print (s1,s2)
		if s1<s2:
			x.append("1")
			return 2**(t-bit-1)+s1
		else:
			x.append("0")
			return 2**(t-bit-1)+s2



n=int(input())
l=list(map(int,input().split()))
l.sort()
t=len(bin(l[-1])[2:])
for i in range(n):
	b=bin(l[i])[2:]
	l[i]="0"*(t-len(b))+b
# print (l)
ans=[]
x=[]
print (solve(l,0))
# print (x)