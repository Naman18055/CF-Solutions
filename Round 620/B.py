n,m=map(int,input().split())
l=[]
for i in range(n):
	l.append(input())
d={}
check={}
mid=""
midlength=0
for i in range(n):
	flag=0
	if l[i] not in check:
		for j in range(i+1,n):
			if l[i]==l[j][::-1]:
				d[l[i]]=l[j]
				check[l[i]]=1
				check[l[j]]=1
				flag=1
		if flag==0:
			if l[i]==l[i][::-1]:
				if len(l[i])>midlength:
					midlength=len(l[i])
					mid=l[i]
#print (d)
p1=""
p2=""
count=0
for i in d:
	p1+=i
	count+=len(i)
print (count*2+midlength)
print (p1+mid+p1[::-1])