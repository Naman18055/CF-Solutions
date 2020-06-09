import math
for nt in range(int(input())):
	n=int(input())
	m=2*n
	a=((m-2)*180)/m
	s=180-a
	t=s
	ans=0
	temp=math.cos((s*math.pi)/180)
	for i in range((n-2)//2):
		# print (t,ans)
		ans+=(math.cos((t*math.pi)/180))
		t+=s
	print (ans*2+1+2*(math.sin((s*math.pi)/180))-math.sin(s*math.pi/360))
