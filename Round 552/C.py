a,b,c=map(int,input().split())
x=a//3
y=b//2
z=c//2
count=0
temp=min(x,y,z)
a=a-temp*3
b=b-temp*2
c=c-temp*2
count+=temp*7
if a>=3:
	a=3
if b>=2:
	b=2
if c>=2:
	c=2
if a==2 and b==2:
	if c==2:
		count+=6
	if c==1:
		count+=5
	if c==0:
		count+=4
if a==3 and b==1:
	if c==2:
		count+=6
	if c==1:
		count+=5
	if c==0:
		count+=3
if a==3 and b==2:
	if c==1:
		count+=6
	if c==0:
		count+=4
if a==2 and b==1:
	if c==2:
		count+=5
	if c==1:
		count+=4
	if c==0:
		count+=3
if a==1 and b==2:
	if c==2:
		count+=5
	if c==1:
		count+=3
	if c==0:
		count+=2
if a==1 and b==1:
	if c==2:
		count+=4
	if c==1:
		count+=3
	if c==0:
		count+=2
if a==1 and b==0:
	if c==2:
		count+=3
	if c==1:
		count+=2
	if c==0:
		count+=1
if a==0 and b==1:
	if c==2:
		count+=2
	if c==1:
		count+=2
	if c==0:
		count+=1
if a==2 and b==0:
	if c==2:
		count+=3
	if c==1:
		count+=2
	if c==0:
		count+=2
if a==0 and b==0:
	if c==2:
		count+=1
	if c==1:
		count+=1
	if c==0:
		count+=0
print (count)
