import sys
input = sys.stdin.readline
from collections import Counter
n,k=map(int,input().split())
l=list(map(int,input().split()))
s=list(set(l))
s.sort()
c=Counter(l)
count=[]
for i in s:
	count.append(c[i])
frwd=[c[s[0]]]
cfrwd=[0]
bckwd=[c[s[-1]]]
cbckwd=[0]
n=len(s)
for i in range(1,n):
	if i==n-1:
		cfrwd.append(cfrwd[-1]+(s[i]-s[i-1])*min(frwd[-1],c[s[-1]]))
		frwd.append(len(l))
		continue
	cfrwd.append((s[i]-s[i-1])*frwd[-1]+cfrwd[-1])
	frwd.append(count[i]+frwd[-1])
for i in range(n-2,-1,-1):
	if i==0:
		cbckwd.append(cbckwd[-1]+(s[i+1]-s[i])*min(bckwd[-1],c[s[0]]))
		bckwd.append(len(l))
		continue
	cbckwd.append((s[i+1]-s[i])*bckwd[-1]+cbckwd[-1])
	bckwd.append(count[i]+bckwd[-1])

# print (s)
# print (count)
# print (frwd)
# print (cfrwd)
# print (bckwd)
# print (cbckwd)
ans=0
try:
	for i in range(n):
		if frwd[i]==k:
			ans=cfrwd[i]
			break
		elif frwd[i]>k:
			num=cfrwd[i]-cfrwd[i-1]
			deno=frwd[i]-frwd[i-1]
			temp=num//deno
			ans=cfrwd[i-1]+(temp*(k-frwd[i-1]))
			break
except:
	flag=1

mans=ans

try:
	for i in range(n):
		if bckwd[i]==k:
			ans=cbckwd[i]
			break
		elif bckwd[i]>k:
			num=cbckwd[i]-cbckwd[i-1]
			deno=bckwd[i]-bckwd[i-1]
			temp=num//deno
			ans=cbckwd[i-1]+(temp*(k-bckwd[i-1]))
			break
except:
	flag=1

ans2=10**18

counts=0
try:
	for i in range(n):
		# print (frwd[i],bckwd[n-i-1],s[i])
		if (frwd[i]+bckwd[n-i-1]-count[i])==k:
			counts=cbckwd[n-i-1]+cfrwd[i]
			# counts=min(cfrwd[i]+cbckwd[n-i-2],counts)
			ans2=min(counts,ans2)
		elif (frwd[i]+bckwd[n-i-2]-count[i])>k:

			num=cbckwd[i]-cbckwd[i-1]
			deno=bckwd[i]-bckwd[i-1]
			temp=num//deno
			counts=cbckwd[i-1]+(temp*(k-bckwd[i-1]))+cfrwd[i-1]

			num=cfrwd[i]-cfrwd[i-1]
			deno=frwd[i]-frwd[i-1]
			temp=num//deno
			counts=min(counts,cfrwd[i-1]+(temp*(k-frwd[i-1]))+cbckwd[i-1])

			ans2=min(counts,ans2)
	# print (counts)
except:
	flag=1

# print (mans,ans,ans2)
print (min(mans,ans,ans2))

