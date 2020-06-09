pre=[1]
s=1
for i in range(1,31):
	pre.append(s+(2**i)*(s+1))
	s=pre[-1]
# print (psre)
for nt in range(int(input())):
	d,m=map(int,input().split())
	if d==1:
		print (1%m)
		continue
	if d==2:
		print (3%m)
		continue
	arr=[]
	s=0
	ans=0
	for i in range(30):
		if s+2**i<=d:
			ans=max(ans,pre[i])
			s+=2**i
		else:
			rem=d-s
			break
	# print (ans,rem)
	ans+=(ans+1)*(rem)
	print (ans%m)
	# for i in range(1,)