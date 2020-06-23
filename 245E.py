s=input()
count=0
# m=0÷
# extr÷a=0
a,b=0,0
for i in s:
	if i=="+":
		count+=1
	else:
		count-=1
	a=min(a,count)
	b=max(b,count)
print (b-a)