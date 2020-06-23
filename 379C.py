import sys
input = sys.stdin.readline
n=int(input())
l=raw_input().split()
new=[]
for i in range(n):
	new.append((int(l[i]),i))
new.sort()
ans=[0]*n
curr=0
for i in range(n):
	curr=max(curr,new[i][0])
	ans[new[i][1]]=curr
	curr+=1
print (' '.join(map(str,ans)))