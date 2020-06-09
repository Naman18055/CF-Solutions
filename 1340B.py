def comp(a,b):
	b=d[b]
	count=0
	for i in range(7):
		if a[i]=="1" and b[i]=="0":
			return -1
		elif a[i]=="0" and b[i]=="1":
			count+=1
	return count

n,count=map(int,input().split())
l=[]
d=["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
num=set(d)
for i in range(n):
	l.append(input())
dp=[[-1 for i in range(9)] for j in range(n)]
for i in range(n):
	for j in range(1,8):
		for k in range(10):
			if comp(l[i],k)==j:
				dp[i][j]=k
for i in range(n):
	if l[i] in num:
		dp[i][0]=d.index(l[i])
minn=0
number=[-1]*n
value=[0]*n
for i in range(n):
	for j in range(8):
		if dp[i][j]!=-1:
			minn+=j
			value[i]=j
			number[i]=(dp[i][j])
			break
# print (minn,number,value)
# for i in dp:
# 	print (*i)
if count<minn:
	print (-1)
	exit(0)


count-=minn
if count!=0:
	for i in range(n):
		m=max(dp[i][value[i]:min(8,value[i]+count+1)])
		ind=dp[i].index(m)
		number[i]=m
		count-=ind-value[i]
		value[i]=ind
		# print (count,number,value)
number1=[]
number2=[]
value1=[]
value2=[]
count1,count2=count,count
for i in range(n):
	number2.append(number[i])
	number1.append(number[i])
	value1.append(value[i])
	value2.append(value[i])
if count1!=0:
	for i in range(n-1,-1,-1):
		for j in range(7,value1[i],-1):
			if count1>=j-value1[i] and dp[i][j]!=-1:
				number1[i]=dp[i][j]
				value1[i]=j
				count1-=1
				break
		if count1==0:
			break
# print (count2)
if count2!=0:
	if count2==1:
		for i in range(n-1,-1,-1):
			if count2==1:
				for j in range(value2[i]+2,8):
					if dp[i][j]!=-1:
						number2[i]=dp[i][j]
						value2[i]=j
						count2-=2
						break
			else:
				if dp[i][value2[i]-1]!=-1:
					number2[i]=dp[i][value2[i]-1]
					value2[i]-=1
					count2+=1
					break
# print (number2,count2,number1,count1)
if count1!=0 and count2!=0:
	print (-1)
	exit()
elif count1!=0 or count2!=0:
	if count1==0:
		print ("".join(map(str,number1)))
	else:
		print ("".join(map(str,number2)))
else:
	ans1="".join(map(str,number1))
	ans2="".join(map(str,number2))
	if ans1>ans2:
		print (ans1)
	else:
		print (ans2)
