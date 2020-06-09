n=int(input())
l=list(map(int,input().split()))
if n==1:
	print (0)
	exit(0)
x=l.count(0)
if x==n:
	print (1)
	exit()
odd,even=0,0
for i in l:
	if i!=0 and i%2==0:
		even+=1
	elif i!=0 and i%2==1:
		odd+=1
odd=(n+1)//2-odd
even=n//2-even
ans=0
prev=-1
nxt=-1
for i in range(n):
	if l[i]!=0:
		if prev==-1:
			prev=i
		else:
			nxt=i
			if l[prev]%2==l[nxt]%2:
				if l[prev]%2==0:
					if (nxt-prev-1)<=even:
						even-=(nxt-prev-1)
					else:
						ans+=2
				else:
					if (nxt-prev-1)<=odd:
						odd-=(nxt-prev-1)
					else:
						ans+=2
			else:
				ans+=1
			prev=i

initial=0
last=0
for i in range(n):
	if l[i]==0:
		initial+=1
	else:
		break
for i in range(n-1,-1,-1):
	if l[i]==0:
		last+=1
	else:
		break
#print (initial,last,odd,even)
if l[initial]%2==1 and odd>=initial:
	odd-=initial
elif l[initial]%2==0 and even>=initial:
	even-=initial
else:
	ans+=1
if l[n-last-1]%2==1 and odd>=last:
	odd-=last
elif l[n-last-1]%2==0 and even>=last:
	even-=last
else:
	ans+=1
print (ans)


