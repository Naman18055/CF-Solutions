import sys
input = sys.stdin.readline

def check(num):
	count1=0
	count2=0
	spent=0
	left=[]
	for i in l:
		if i[0]>num:
			count2+=1
			spent+=i[0]
		elif i[1]<num:
			count1+=1
			spent+=i[0]
		else:
			left.append(i)
	# if num==36:
		# print (num,left,spent,count2,count1)
	if count2>n//2+1:
		return True
	elif count1>n//2:
		return False
	else:
		# print (num,left,spent,count2,count1)
		for i in left:
			if count2!=n//2+1:
				spent+=num
				count2+=1
			else:
				spent+=i[0]
				count1+=1
		# print (num,left,spent,count2,count1)
		if count2==n//2+1 and count1==n//2 and spent<=s:
			return True
		return False

for nt in range(int(input())):
	n,s=map(int,input().split())
	l=[]
	for i in range(n):
		a,b=map(int,input().split())
		l.append((a,b))
	l.sort(reverse=True)
	if n==1:
		print (min(l[0][1],s))
		continue
	low=0
	high=10**10
	while low<high:
		mid=(low+high)//2
		if check(mid):
			low=mid+1
		else:
			high=mid-1
	if check(low):
		print (low)
	else:
		print (low-1)