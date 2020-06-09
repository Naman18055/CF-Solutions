n=int(input())
l=[]
ans=0
for i in range(n):
	l.append(int(input()))
def rec(a,l):
	global ans
	if len(l)==0:
		if a%360==0:
			ans=1
			return 1
		else:
			return 0
	else:
		return rec(a-l[0],l[1:])+rec(a+l[0],l[1:])
rec(2880,l)
if ans==1:
	print ("YES")
else:
	print ("NO")