from bisect import bisect_left, bisect_right

a,b,c,d=map(int,input().split())
length=c-b+1
r=[c,d]
ans=0
for i in range(a,b+1):
	first=i
	s=[b-i+1,i+b-1]
	e=[c-i+1,i+c-1]
	start1=max(c,s[0])
	end1=min(d,s[1])
	start2=max(c,e[0])
	end2=min(d,e[1])
	s1=max(end1-c+1,1)
	s2=min(s[1]-s[0]+1,min(end2,d)-c+1)
	s3=max(min(d,end2)-start2+1,1,)
	if s2<1:
		ans+=0
	else:
		if e[0]<=c:
			if e[1]<=d:
				t=1
			else:
				t=min(e[1]-d+1,c-b+1)
		else:
			print (1/0)
			t=min(c-b+1,max(e[0]-c+1,e[1]-d+1))
		temp=((s2-1)*s2)//2-(((s1-1)*s1)//2)
		temp+=max(0,((s2-1)*s2)//2-(((s3-1)*s3)//2))
		temp+=s2*t
		ans+=temp
		# print (s,e,t)
		# print (i,s1,s2,s3,temp)
print (ans)
# ans=0
# dic2={z:0 for z in range(c,min(d,b+c-1)+1)}
# for z in range(c,min(d,b+c-1)+1):
# 	if 2*b>=z+1:
# 		if a>=z+1-b:
# 			ans+=((b-a)+1)*((c-b)+1)
# 			dic2[z]=((b-a)+1)*((c-b)+1)
# 		elif a>=z+1-c:
# 			ans+=(b+c-z)*(b+c+1-z)//2-(2*b-z)*(2*b-z-1)//2-(a+c-z)*(a+c-z-1)//2
# 			dic2[z]=(b+c-z)*(b+c+1-z)//2-(2*b-z)*(2*b-z-1)//2-(a+c-z)*(a+c-z-1)//2
# 		else:
# 			ans+=(b+c-z)*(b+c+1-z)//2-(2*b-z)*(2*b-z-1)//2
# 			dic2[z]=(b+c-z)*(b+c+1-z)//2-(2*b-z)*(2*b-z-1)//2
# 	else:
# 		if a>=z+c-1:
# 			ans+=(b+c-z)*(b+c+1-z)//2-(a+c-z)*(a+c-z-1)//2
# 			dic2[z]=(b+c-z)*(b+c+1-z)//2-(a+c-z)*(a+c-z-1)//2
# 		else:
# 			ans+=(b+c-z)*(b+c+1-z)//2
# 			dic2[z]




