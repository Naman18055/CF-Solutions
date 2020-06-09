def calc(num):
	n=str(num)
	ans=0
	for i in n:
		ans+=int(i+i)
	return ans

n=int(input())
sums=[0 for i in range(9)]
zero=[1 for i in range(9)]
ans=0
num=input().split()
ans+=calc(num[0])
j=8
for i in num[0]:
	sums[j]=i
	zero[j]=0
	j-=1

for i in range(1,n):
	ans+=calc(num[i])
	count=[i]*len(num[[i]])
	carry=0
	add1=[0]*18
	k=17
	for j in range(len(num[i])-1,-1,-1):
		a=num[i][j]*count[j]+carry
		add[k]=int(str(a)[-1])
		carry=int(str(a)[0:-1])
		k-=1
		add[k]=sum(k//2)
		count[j-1]-=zero[k//2]
		print (add,a,ans)
	for j in range(len())

