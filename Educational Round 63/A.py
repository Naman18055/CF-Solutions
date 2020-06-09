n=int(input())
s=input()
flag=0
for i in range(n-1):
	if s[i+1]<s[i]:
		print ('YES')
		flag=1
		print (i+1,i+2)
		break
if flag==0:
	print ('NO')