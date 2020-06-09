import sys
input = sys.stdin.readline

def mult_input():
	return map(int,input().split())

def list_input():
	return list(map(int,input().split()))

prime=[[] for i in range(200001)]
for i in range(2,200001):
	if len(prime[i])==0:
		for j in range(i,200001,i):
			prime[j].append(i)
# print (prime)
n=int(input())
l=list_input()
s=[]
location={}
for i in range(n):
	for j in prime[l[i]]:
		if j not in location:
			location[j]={i:0}
		if True:
			m=l[i]
			while m%j==0:
				if i not in location[j]:
					location[j][i]=1
				else:
					location[j][i]+=1
				m=m//j
		s.append(j)
s=set(s)
# print (s)
# print (location)
ans=1
for i in s:
	if len(location[i])<n-1:
		continue
	else:
		m=10**9
		for j in location[i]:
			m=min(location[i][j],m)
	if len(location[i])==n-1:
		ans=ans*(i**m)
		continue
	count=0
	for j in location[i]:
		if location[i][j]==m:
			count+=1
	if count>=2:
		ans=ans*(i**(m))
		continue
	minn=10**9
	for j in location[i]:
		if location[i][j]>m:
			minn=min(minn,location[i][j])
	ans=ans*(i**(minn))
	# print (m,minn)
print (ans)
