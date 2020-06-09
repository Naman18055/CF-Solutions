import sys
input = sys.stdin.readline
n=int(input())
l=[]
l2=[]
l3=[]
count=0
for i in range(n):
	l.append(input())


def crr(a,n):
    if len(a)==0 and n==0:
        return True
    elif len(a)==0:
        return False
    if n<0:
        return False
    else:
        if a[0]=="(":
            n+=1
        else:
            n-=1
    return crr(a[1:],n)

for i in range(len(l)):
	for j in range(len(l)):
		if i!=j:
			if i not in l2 and j not in l2:
				if crr(l[i]+l[j],0):
					l2.append(i)
					l2.append(j)
					count+=1

print (count)

