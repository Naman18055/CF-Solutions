import collections
def cal(n):
	return (n*(n-1)//2)

n=int(input())
l=[]
for i in range(n):
	l.append((input())[0])
	d=collections.Counter(l)
count=0
for i in d:
	if d[i]%2==0:
		count+=(cal(d[i]//2))
		count+=(cal(d[i]//2))
	else:
		count+=(cal((d[i]-1)//2))
		count+=(cal((d[i]+1)//2))
print (count)
