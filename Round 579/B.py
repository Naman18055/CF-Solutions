from collections import Counter
import math

t=int(input())
for nt in range(t):
	n=int(input())
	l=list(map(int,input().split()))
	cnt = Counter(l)
	flag=0
	for i in cnt:
		if cnt[i]%2==1:
			print ("NO")
			flag=1
			break
	if flag==0:
		temp=[]
		for i in cnt:
			for j in range(cnt[i]//2):
				temp.append(i)
		temp.sort()
		flag=0
		area=temp[0]*temp[-1]
		for i in range(len(temp)//2):
			if temp[i]*temp[len(temp)-i-1]!=area:
				print ("NO")
				flag=1
				break
		if flag==0:
			print ("YES")
			

