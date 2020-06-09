def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

def comp(a,b):
	ans=0
	for i in range(7):
		if a[i]=="1" and b[i]!="1":
			return -1
		elif a[i]=="0" and b[i]=="1":
			ans+=1
	return ans

n,k=mult_input()
l=[]
for i in range(n):
	l.append(input())
if k>n*7:
	print (-1)
	exit()
num=["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]

reqd=[9]*n
least=[0]*n
for i in range(n-1,-1,-1):
	least[i]=7-l[i].count("1")
	for j in num:
		number=comp(l[i],j)
		if number!=-1:
			reqd[i]=min(reqd[i],number)
print (reqd)


left=[0]*n
maxx=[0]*n
left[-1]=reqd[-1]
maxx[-1]=least[-1]
for i in range(n-2,-1,-1):
	left[i]=left[i+1]+reqd[i]
	maxx[i]=maxx[i+1]+least[i]
print (left)
print (maxx)


if left[0]>k or k>sum(least):
	print (-1)
	exit()

ans=""
for i in range(n-1):
	rem = k-left[i+1]
	sta = k-maxx[i+1]
	m,mu=-1,-1
	for j in range(10):
		used=comp(l[i],num[j])
		# print (j,used,rem,sta)
		if used!=-1 and used<=rem and used>=sta:
			if j>m:
				m=j
				mu=used
				# print (m,mu)
	if m==-1:
		print (-1)
		exit()
	ans+=str(m)
	k-=mu
	print (ans)
# print (k)
m=-1
rem=k
for j in range(10):
	used=comp(l[-1],num[j])
	if used==rem:
		if j>m:
			m=j
if m==-1:
	print (-1)
	exit()

ans+=str(m)
print (ans)


