n=int(input())
s=input()
count=0
x=''
y=0
for i in range(len(s)):
	for j in range(i+1,len(s)+1):
		x=s[0:i]+s[j:]
		if len(x)>0:
			a=x[0]
			if x.count(a)!=len(x):
				y=1
		if y==0:
			count+=1
		else:
			y=0
print (count%998244353)

