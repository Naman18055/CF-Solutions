import sys
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a


n=int(input())
l=list(input())[:n]
if n>=1:
	while(len(l)>1):
		a=0
		idx=-1
		f=False
		if l[0]-1==l[1]:
			f=1
			idx=0
			a=l[0]
			idx=0
		
		for i in range(1,len(l)-1):
			if l[i]-l[i-1]==1 or l[i]-l[i+1]==1:
				f=True
				if l[i]>a:
					a=max(a,l[i])
					idx=i
		if l[-1]-l[-2]==1:
			f=True
			if l[-1]>a:
				a=max(a,l[-1])
				idx=-1
		if not f:break
		# print(l)
		# print(idx)
		l.pop(idx)
# print(l)
print(n-len(l))




