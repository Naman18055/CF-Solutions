for nt in range(int(input())):
	p,f = map(int,input().split())
	c1,c2 = map(int,input().split())
	s,w = map(int,input().split())
	p,f = max(p,f),min(p,f)
	if s>w:
		w,s = s,w
		c1,c2 = c2,c1
	
	ans = 0
	for i in range(c1+1):
		if i*s<=p:
			ans = max(ans,i+min(c2,(p-i*s)//w)+min(c1-i,f//s)+min(max(0,c2-(p-i*s)//w),max(0,f-(c1-i)*s)//w))
	print (ans)