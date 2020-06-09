import sys
input = sys.stdin.readline
t=int(input())
for nt in range(t):
	x=int(input())
	s=(input())
	n=len(s)
	c=s[1:]
	p=0
	ans=n
	flag=0
	while p<x:
		p+=1
		if len(s)<x:
			c=s[p:]
			ans=p
			ans+=((len(c)*(int(s[p-1])))%1000000007)
			#ans=ans%1000000007
			#s+=(c*(int(s[p-1])-1))
			for i in range((int(s[p-1])-1)):
				for j in c:
					s+=j
					if len(s)>x:
						break
				if len(s)>x:
					break
		else:
			if flag==0:
				c=len(c)
				flag=1
			c=(ans-p)
			ans=p
			ans+=((c*int(s[p-1]))%1000000007)
			#ans=ans%1000000007
		#print (ans,c,s)
	#print (s)
	#print (len(s))
	print (ans%1000000007)

