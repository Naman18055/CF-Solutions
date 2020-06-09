import sys
input = sys.stdin.buffer.readline
for nt in range(int(input())):
	h,c,t=map(int,input().split())
	m=(h+c)/2
	if m>=t:
		print (2)
		continue
	if h<t:
		print (1)
		continue
	# h*x + c*(x-1) = t*(2*x-1)
	# x*(h+c)=2tx-t+c
	# t-c=x*(2t-h-c)
	m=10**18
	x = (t-c)/(2*t-h-c)
	# print (x)
	for i in range(max(1,int(x-10)),int(x+10)):
		# print (i,abs(t*(2*i-1)-((h*i+c*(i-1)))),t*(2*i-1),h*i+c*(i-1))
		if abs(t*(2*i-1)-((h*i+c*(i-1))))/(2*i-1)<m:
			m=abs(t*(2*i-1)-((h*i+c*(i-1))))/(2*i-1)
			ans=2*i-1			
	print (ans)