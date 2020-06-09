import sys
from collections import deque
input = sys.stdin.readline

def f(l):
	count1,count2,count3=0,0,0
	start="R"
	prev="B"
	for i in range(len(l)):
		if l[i]!=start:
			count1+=1
		prev=start
		if start=="R":
			start="G"
		elif start=="G":
			start="B"
		else:
			start="R"
	#print (count1)
	start="G"
	prev="R"
	for i in range(len(l)):
		if l[i]!=start:
			count2+=1
		prev=start
		if start=="R":
			start="G"
		elif start=="G":
			start="B"
		else:
			start="R"
	#print (count2)
	start="B"
	prev="G"
	for i in range(len(l)):
		if l[i]!=start:
			count3+=1
		prev=start
		if start=="R":
			start="G"
		elif start=="G":
			start="B"
		else:
			start="R"
	#print (count3)
	#print (min(count1,count2,count3))
	return min(count1,count2,count3)

t=int(input())
# st="RGB"
# for i in range(666):
# 	st+=("RGB")
for nt in range(t):
	n,k=map(int,input().split())
	s=input()
	temp=list(s[0:k])
	temp=deque(temp)
	m=1000000
	temp2=f(temp)
	if temp2<m:
		m=temp2
	for i in range(k,n):
		temp.popleft()
		temp.append(s[i])
		#print (temp)
		temp2=f(temp)
		#print (temp,temp2)
		if temp2<m:
			m=temp2
	print (m)


